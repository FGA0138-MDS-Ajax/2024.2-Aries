import base64
import calendar
import locale
from datetime import date, datetime, timedelta
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.core.files.images import ImageFile
from django.db.models import Count, Q
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.dateparse import parse_date
from django.utils.timezone import localtime, make_aware

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from .forms import EventForm, PostForm, TaskForm
from .models import (
    Area, Column, Event, MembroEquipe, Meeting, Post, Subtask, Task
)
from .serializers import ColumnSerializer, TaskSerializer


locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')


def sidebar(request):
     members = MembroEquipe.objects.all()
     return render(request,"partials/_sidebar.html", {'members':members})


def Top(request):
     return render(request, 'partials/Top.html')

@login_required
def create_post_or_event(request):
    
    if request.user.is_authenticated:
        member = request.user
    
    if request.method == "POST":
        # Verifica se é um evento
        is_event = request.POST.get('is_event', False)

        if is_event:  # Se for um evento
            # Criação do evento
            event_form = EventForm(request.POST)
            if event_form.is_valid():
                event = event_form.save(commit=False)
                event.member = member
                event.save()   # Salva o evento
                
        else:  # Se for apenas um post
            # Criação do post
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.member = member
                post.save()
                return redirect('home')  # Redireciona para a lista de posts
            else:
                return redirect('home')
    else:
        post_form = PostForm()
        event_form = EventForm()
   

    return redirect('home')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid(): 
         task = form.save()  # Salva a tarefa
                 # Salva os relacionamentos ManyToMany
    else:
            form = TaskForm()



def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('id_task')
                
        if task_id:
            task = get_object_or_404(Task, id=task_id)
            task.delete()  # Deleta a task
        return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect(request.META.get('HTTP_REFERER', '/'))

def edit_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('id_task')
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        prazo = request.POST.get('Prazo')
        responsible = request.POST.get('responsibles')

        # se não for enviada o id da task, não é possivel fazer a edição.
        if not task_id:
            return HttpResponseBadRequest("ID da tarefa não fornecido")
        task = get_object_or_404(Task, id=task_id)

        if responsible:
            responsible = list(map(int, responsible.split(',')))
            responsible_members = MembroEquipe.objects.filter(id__in=responsible)
            task.responsible.set(responsible_members)
            

        # atualiza os dados da tarefa se eles forem solicitados a edição
        task.title = title if title else task.title
        task.description = description if description else task.description
        task.priority = priority if priority else task.priority
        task.Prazo = prazo if prazo else task.Prazo
        task.save()

        # pegar um vetor dos nomes/labels da checkbox e um vetor de true e false como string referente as checkbox (essa parte de true ou false foi feita no js)
        subtasks_list = request.POST.getlist('inputTask')  
        checkbox_input = request.POST.get('inputSubTask')  

        # filtra as subtarefas vazias e processa os checkboxes, evitando assim dados inconsistentes
        subtasks_list = [subtask for subtask in subtasks_list if subtask.strip()]


        #se checkbox_input for none, significa que foi requisição via ajax para alterar somente as checkbox
        if checkbox_input is None:
            subtasks_status = {}

            for key, value in request.POST.items():
                if key.startswith('checkbox-subtask-'):
                    subtask_id = key.split('-')[-1]  # Extrai o ID da subtask
                    status = value == 'on'  # Marca como 'True' se estiver marcado, caso contrário 'False'
                    subtasks_status[subtask_id] = status

            # Atualiza o status das subtarefas associadas à tarefa
            for subtask_id, done in subtasks_status.items():
                subtask = get_object_or_404(Subtask, id=subtask_id)
                subtask.done = done
                subtask.save()

            return redirect(request.META.get('HTTP_REFERER', '/'))

        #se checkbox not is none, significa que foi solicitada uma requisição de edição que sobrescreve os dados anteriores, por isso o delete para depois sobrescrever.
        task.subtasks.all().delete()
        if checkbox_input:
            checkbox_input = checkbox_input.split(',')
            # converte as strings 'true'/'false' para valores booleanos
            checkbox_input = [True if item == 'true' else False for item in checkbox_input]
            
            for subtask_title, done_status in zip(subtasks_list, checkbox_input):
                Subtask.objects.create(
                    description=subtask_title,  
                    task=task,                  
                    done=done_status            
                )
            return redirect(request.META.get('HTTP_REFERER', '/'))

    return redirect(request.META.get('HTTP_REFERER', '/'))

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        column_id = self.request.query_params.get('column')
        if column_id:
            return self.queryset.filter(column_id=column_id)
        return self.queryset

def image_to_base64(image):
    """
    Converte a imagem do campo ImageField para uma string base64.
    Lida tanto com arquivos de imagem quanto com dados binários.
    """
    if isinstance(image, bytes):  # Se image já for um objeto de bytes
        return base64.b64encode(image).decode('utf-8')
    
    if image:
        with open(image.path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
        

@login_required
def kanban_view(request):
    # Obtém a área a partir dos parâmetros da URL (GET)
    area_id = request.GET.get('area')  # Exemplo: ?area=SE
    
    # Filtra as tarefas pela área, se especificada
    if area_id:
        # Filtra as tarefas pela área especificada na URL
        tasks = Task.objects.filter(area__id=area_id)
    else:
        # Caso nenhuma área seja especificada, exibe todas as tarefas
        tasks = Task.objects.all()  # Caso nenhuma área seja especificada, retorna todas as tarefas
    
    items = []
    members = []
    all_areas = Area.objects.all().order_by('name')
    profiles = MembroEquipe.objects.all()

    for profile in profiles:
        if profile.photo:
            profile.photo_base64 = image_to_base64(profile.photo)
        else:  
            profile.photo_base64 = None
            

    if area_id:
        profileFiltered = MembroEquipe.objects.filter(area=area_id);
    else:
        profileFiltered = MembroEquipe.objects.all();

    for profile in profileFiltered:
        
        areas = [area.name for area in profile.area.all()]
        members.append({
            'email': profile.email,
            'fullname': profile.fullname,
            'username': profile.username,
            'photo': profile.photo,
            'area': ", ".join(areas),
        })

    members_count = len(members)-5

    total_tasks = tasks.count()
    completed_task_count = tasks.filter(status='Concluída').count()
    Em_Progresso_task_count = tasks.filter(status='Em Progresso').count()
    Pendente_count = tasks.filter(status='Pendente').count()
    
    if total_tasks > 0:
        pending_percentage = round((Pendente_count / total_tasks) * 100)
        in_progress_percentage = round((Em_Progresso_task_count / total_tasks) * 100)
        completed_percentage = round((completed_task_count / total_tasks) * 100)
    else:
        pending_percentage = in_progress_percentage = completed_percentage = 0
    
    # Processa as tarefas
    
    for task in tasks:
        prazo = task.Prazo
        today = datetime.now().date()
        dateTask = prazo.strftime("%d / %m / %Y")
        if prazo:
            if prazo == today:
                formatted_date = "HOJE"
            else:
                formatted_date = prazo.strftime("%d / %m / %Y")
        else:
            formatted_date = "Sem prazo definido"

        responsible_profiles = task.responsible.all()
        responsible_photos = []
        
        for resp in responsible_profiles:
            if resp.photo:
                responsible_photos.append(image_to_base64(resp.photo))
            else:
                responsible_photos.append(None)
                
        subtasks = Subtask.objects.filter(task=task)

        subtask_completed_count = 0
        subtask_total_count = 0
        
        for subtask in subtasks:
            checkbox = request.POST.get('checkbox-subtask')
            if subtask.done == True:
                subtask_completed_count += 1
                subtask_total_count += 1
            else: 
                subtask_total_count += 1

        pair_r_p = list(zip(task.get_responsibles(), responsible_photos))


        items.append({
            'id': task.id,
            'status': task.status,
            # 'area': task.area.all,
            'title': task.title,
            'description': task.description,
            'creation_date': task.creation_date,
            'priority': task.priority,
            'prazo': formatted_date,
            'date': dateTask,
            'completion_date': task.completion_date,
            'responsible': task.get_responsibles_as_string(),
            'responsible_photos': responsible_photos,
            'responsible_count': task.responsible.count(),
            'subtask_completed_count': subtask_completed_count,
            'subtask_total_count': subtask_total_count,
            'pair_responsible_photo': pair_r_p,
            'subtasks': subtasks,
        })
    
    
    # Adicionar nova tarefa via POST
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        prazo = request.POST.get('Prazo') or None
        area_id = request.POST.get('area_id')
        responsible = request.POST.get('responsibles')
        subtasks_list = request.POST.getlist('inputTask')
        checkbox_input = request.POST.get('inputSubTask')

        
        task = Task.objects.create(
            title=title,
            description=description,
            status=status,
            priority=priority,
            Prazo=prazo,
        )

        task.area.set(area_id)

        if checkbox_input:
            subtasks_list = [elemento for elemento in subtasks_list if elemento != ""]
            checkbox_input= checkbox_input.split(',')
            
            for i in range(len(checkbox_input)):
                if checkbox_input[i] == 'true':
                    checkbox_input[i] = True
                else:
                    checkbox_input[i] = False

            for subtask_title, done_status in zip(subtasks_list, checkbox_input):
                subtask = Subtask.objects.create(
                    description=subtask_title,  # Associa o título da subtarefa
                    task=task,                   # Associando à task recém-criada
                    done=done_status             # Define o estado do checkbox
                )
    
        if responsible:
            responsible = list(map(int, responsible.split(',')))
            responsible_members = MembroEquipe.objects.filter(id__in=responsible)
            task.responsible.set(responsible_members)
        
        return redirect(request.get_full_path())
    
    return render(request, 'kanbam.html', {
        'items': items,
        'profiles': profiles,
        'members': members,
        'selected_area': area_id,
        'all_areas': all_areas,
        'completed_task_count': completed_task_count,
        'Em_Progresso_task_count': Em_Progresso_task_count,
        'Pendente_count':  Pendente_count,
        'pending_percentage': pending_percentage,
        'in_progress_percentage': in_progress_percentage,
        'completed_percentage': completed_percentage,
        'members_count': members_count
    })



@api_view(['PATCH'])
def update_task_status(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    

    new_status = request.data.get('status')
    if not new_status:
        return Response({"error": "Status not provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    task.status = new_status
    task.save()

    serializer = TaskSerializer(task)
    return Response(serializer.data, status=status.HTTP_200_OK)

    
def upload_photo(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        photo = request.FILES['photo']  # Obtém o arquivo enviado
        photo_data = photo.read()  # Lê os dados binários do arquivo

        # Salva no banco
        profile = MembroEquipe(fullname=fullname, photo=photo_data,email=email,phone=phone,username=fullname)
        profile.save()

        return redirect('profile_list')  # Redireciona para outra página
    return render(request, 'upload_photo.html')

def profile_list(request):
    profiles = MembroEquipe.objects.all()
    for profile in profiles:
        # Converte o blob em uma string Base64
        if profile.photo:
            profile.photo_base64 = base64.b64encode(profile.photo).decode('utf-8')
    return render(request, 'profile_list.html', {'profiles': profiles})



@login_required
def home(request):
    announcements = Post.objects.all().order_by('-posted_at')
    all_events = Event.objects.all().distinct()
    selected_date = request.GET.get('date')
    now = datetime.strptime(selected_date, '%Y-%m-%d') if selected_date else datetime.now()

    year, month, day = now.year, now.month, now.day
    current_year = datetime.now().year

    for event in all_events:
        if event.event_date:
            event.day = event.event_date.day
            event.month = event.event_date.month
            if event.event_date.year == current_year:
                event.formatted_date = event.event_date.strftime("%d de %B")
            else:
                event.formatted_date = event.event_date.strftime("%d de %B de %Y")
        else:
            event.day = None
            event.month = None
        
        if event.event_time:
            event.formatted_time = event.event_time.strftime("%Hh%M")
        else:
            event.formatted_time = None

    filtered_events = Event.objects.filter(
        event_date__year=year,
        event_date__month=month,
        event_date__day=day
    )

    weeks = get_calendar_data(year, month, now, request.user)

    tasks = filters(Task, 'Prazo', year, month, day, request.user)
    meetings = filters(Meeting, 'meeting_date', year, month, day).filter(areas__membros=request.user).distinct()

    user_area = request.user.areas.first()
    meetings_data = get_meeting(meetings)

    context = {
        "now": now,
        "year": year,
        "month": month,
        "month_name": calendar.month_name[month],
        "weeks": weeks,
        "events_obj": filtered_events,  # para o calendário
        "all_events": all_events,  # para o feed
        "announcements": announcements,
        "tasks": tasks,
        "meetings": meetings_data,
        "user_area_color": user_area.color if user_area else '#0075F6',
    }

    return render(request, 'home.html', context)


def get_calendar_data(year, month, now, user):
    cal = calendar.Calendar(firstweekday=6) 
    days = cal.itermonthdays4(year, month) 

    weeks = []
    week = []
    for day in days:
        day_tasks = Task.objects.filter(Prazo__year=day[0], Prazo__month=day[1], Prazo__day=day[2], responsible=user)
        day_events = Event.objects.filter(event_date__year=day[0], event_date__month=day[1], event_date__day=day[2])
        day_meetings = Meeting.objects.filter(meeting_date__year=day[0], meeting_date__month=day[1], meeting_date__day=day[2]).filter(areas__membros=user).distinct()
        
        if day[1] == month:  
            is_today = (day[2] == now.day)
            week.append({
                "day": day[2], 
                "in_month": True, 
                "is_today": is_today,
                "tasks": day_tasks.exists(),
                "events": day_events.exists(),
                "meetings": day_meetings.exists(),
                "meetings_multiple_teams": any(meeting.areas.count() > 1 for meeting in day_meetings)
            })
        else:
            week.append({
                "day": day[2], 
                "in_month": False, 
                "is_today": False,
                "tasks": day_tasks.exists(),
                "events": day_events.exists(),
                "meetings": day_meetings.exists(),
                "meetings_multiple_teams": any(meeting.areas.count() > 1 for meeting in day_meetings)
            })
        
        if len(week) == 7:  
            weeks.append(week)
            week = []

    if week:  
        weeks.append(week)

    return weeks

def get_meeting(meetings):
    meetings_data = []
    for meeting in meetings:
        multiple_teams = meeting.areas.count() > 1
        areas_data = [{"name": area.name, "color": area.color} for area in meeting.areas.all()]
        meetings_data.append({
            "title": meeting.title,
            "time": localtime(meeting.meeting_date).strftime('%Hh%M'),
            "multiple_teams": multiple_teams,
            "areas": areas_data,
        })
    return meetings_data

def filters(model, date_field, year, month, day, user=None):
    filters = {
        f"{date_field}__year": year,
        f"{date_field}__month": month,
        f"{date_field}__day": day,
    }
    if user:
        filters["responsible"] = user
    return model.objects.filter(**filters)

def get_events_tasks(request):
    date_str = request.GET.get('date')
    
    if date_str:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d')
        selected_date = make_aware(selected_date)
        year, month, day = selected_date.year, selected_date.month, selected_date.day

        events = filters(Event, 'event_date', year, month, day)
        tasks = filters(Task, 'Prazo', year, month, day, request.user)
        meetings = filters(Meeting, 'meeting_date', year, month, day).filter(areas__membros=request.user).distinct()

        events_data = [{"title": event.title, "time": event.event_time.strftime('%Hh%M') if event.event_time else None} for event in events]
        tasks_data = [{"title": task.title, "time": localtime(make_aware(datetime.combine(task.Prazo, datetime.min.time()))).strftime('%Hh%M')} for task in tasks]
        meetings_data = get_meeting(meetings)

        return JsonResponse({"events": events_data, "tasks": tasks_data, "meetings": meetings_data})
    else:
        return JsonResponse({"error": "Invalid date"}, status=400)

def previous_month(request):
    current_date = parse_date(request.GET.get('date'))
    if current_date:
        first_day_of_current_month = current_date.replace(day=1)
        previous_month_date = first_day_of_current_month - timedelta(days=1)
        new_date = previous_month_date.replace(day=min(current_date.day, calendar.monthrange(previous_month_date.year, previous_month_date.month)[1]))
        return redirect(f'/home/?date={new_date.strftime("%Y-%m-%d")}')
    return redirect('home')

def next_month(request):
    current_date = parse_date(request.GET.get('date'))
    if current_date:
        last_day_of_current_month = current_date.replace(day=calendar.monthrange(current_date.year, current_date.month)[1])
        next_month_date = last_day_of_current_month + timedelta(days=1)
        new_date = next_month_date.replace(day=min(current_date.day, calendar.monthrange(next_month_date.year, next_month_date.month)[1]))
        return redirect(f'/home/?date={new_date.strftime("%Y-%m-%d")}')
    return redirect('home')

def delete_announcement(request, announcement_id):
    announcement = get_object_or_404(Post, id=announcement_id)
    announcement.delete()
    return redirect('home')

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('home')

def taskBoard(request):
    # Obtém a área a partir dos parâmetros da URL (GET)
    area_id = request.GET.get('area')  # Exemplo: ?area=SE
    
    # Filtra as tarefas pela área, se especificada
    if area_id:
        # Filtra as tarefas pela área especificada na URL
        tasks = Task.objects.filter(area__id=area_id)
    else:
        # Caso nenhuma área seja especificada, exibe todas as tarefas
        tasks = Task.objects.all()  # Caso nenhuma área seja especificada, retorna todas as tarefas
    
    items = []
    members = []
    all_areas = Area.objects.all().order_by('name')
    profiles = MembroEquipe.objects.all()

    for profile in profiles:
        if profile.photo:
            profile.photo_base64 = image_to_base64(profile.photo)
        else:  
            profile.photo_base64 = None
            

    if area_id:
        profileFiltered = MembroEquipe.objects.filter(area=area_id);
    else:
        profileFiltered = MembroEquipe.objects.all();

    for profile in profileFiltered:
        
        areas = [area.name for area in profile.area.all()]
        members.append({
            'email': profile.email,
            'fullname': profile.fullname,
            'username': profile.username,
            'photo': profile.photo,
            'area': ", ".join(areas),
        })

    members_count = len(members)-5

    total_tasks = tasks.count()
    completed_task_count = tasks.filter(status='Concluída').count()
    Em_Progresso_task_count = tasks.filter(status='Em Progresso').count()
    Pendente_count = tasks.filter(status='Pendente').count()
    
    if total_tasks > 0:
        pending_percentage = round((Pendente_count / total_tasks) * 100)
        in_progress_percentage = round((Em_Progresso_task_count / total_tasks) * 100)
        completed_percentage = round((completed_task_count / total_tasks) * 100)
    else:
        pending_percentage = in_progress_percentage = completed_percentage = 0
    
    # Processa as tarefas
    
    for task in tasks:
        prazo = task.Prazo
        today = datetime.now().date()
        dateTask = prazo.strftime("%d / %m / %Y")
        if prazo:
            if prazo == today:
                formatted_date = "HOJE"
            else:
                formatted_date = prazo.strftime("%d / %m / %Y")
        else:
            formatted_date = "Sem prazo definido"

        responsible_profiles = task.responsible.all()
        responsible_photos = []
        
        for resp in responsible_profiles:
            if resp.photo:
                responsible_photos.append(image_to_base64(resp.photo))
            else:
                responsible_photos.append(None)
                
        subtasks = Subtask.objects.filter(task=task)

        subtask_completed_count = 0
        subtask_total_count = 0
        
        for subtask in subtasks:
            checkbox = request.POST.get('checkbox-subtask')
            if subtask.done == True:
                subtask_completed_count += 1
                subtask_total_count += 1
            else: 
                subtask_total_count += 1

        pair_r_p = list(zip(task.get_responsibles(), responsible_photos))


        items.append({
            'id': task.id,
            'status': task.status,
            'title': task.title,
            'description': task.description,
            'creation_date': task.creation_date,
            'priority': task.priority,
            'prazo': formatted_date,
            'date': dateTask,
            'completion_date': task.completion_date,
            'responsible': task.get_responsibles_as_string(),
            'responsible_photos': responsible_photos,
            'responsible_count': task.responsible.count(),
            'responsible_name': task.responsible.count(),
            'subtask_completed_count': subtask_completed_count,
            'subtask_total_count': subtask_total_count,
            'pair_responsible_photo': pair_r_p,
            'subtasks': subtasks,
        })
    
    
    # Adicionar nova tarefa via POST
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        prazo = request.POST.get('Prazo') or None
        area_id = request.POST.get('area_id')
        responsible = request.POST.get('responsibles')
        subtasks_list = request.POST.getlist('inputTask')
        checkbox_input = request.POST.get('inputSubTask')

        
        task = Task.objects.create(
            title=title,
            description=description,
            status=status,
            priority=priority,
            Prazo=prazo,
        )

        task.area.set(area_id)

        if checkbox_input:
            subtasks_list = [elemento for elemento in subtasks_list if elemento != ""]
            checkbox_input= checkbox_input.split(',')
            
            for i in range(len(checkbox_input)):
                if checkbox_input[i] == 'true':
                    checkbox_input[i] = True
                else:
                    checkbox_input[i] = False

            for subtask_title, done_status in zip(subtasks_list, checkbox_input):
                subtask = Subtask.objects.create(
                    description=subtask_title,  # Associa o título da subtarefa
                    task=task,                   # Associando à task recém-criada
                    done=done_status             # Define o estado do checkbox
                )
    
        if responsible:
            responsible = list(map(int, responsible.split(',')))
            responsible_members = MembroEquipe.objects.filter(id__in=responsible)
            task.responsible.set(responsible_members)
        
        return redirect(request.get_full_path())
    
    return render(request, 'taskBoard.html', {
        'items': items,
        'profiles': profiles,
        'members': members,
        'selected_area': area_id,
        'all_areas': all_areas,
        'completed_task_count': completed_task_count,
        'Em_Progresso_task_count': Em_Progresso_task_count,
        'Pendente_count':  Pendente_count,
        'pending_percentage': pending_percentage,
        'in_progress_percentage': in_progress_percentage,
        'completed_percentage': completed_percentage,
        'members_count': members_count
    })
