from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .forms import TaskForm, EventForm, PostForm
from .models import MembroEquipe, Task, Event, Post, Meeting
from rest_framework import viewsets
from .models import Column, Task
from .serializers import ColumnSerializer, TaskSerializer
import calendar
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from django.utils.timezone import localtime
from django.utils.dateparse import parse_date
import locale
import base64

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
        return redirect('kanban')

    return redirect('kanban')


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


def kanban_view(request):
    tasks = Task.objects.all()  
    items = []
    profiles = MembroEquipe.objects.all()
    
    members = []
    
    for profile in profiles:
        # Converte o blob em uma string Base64
        if profile.photo:
            profile.photo_base64 = base64.b64encode(profile.photo).decode('utf-8')

        members.append({
        'email': profile.email,
        'fullname': profile.fullname,
        'username': profile.username,
        'photo':  profile.photo,
        })

    for task in tasks:
        prazo = task.Prazo
        today = datetime.now().date() 
        if prazo:
            if prazo == today:
                formatted_date = "HOJE"
            else:
                formatted_date = prazo.strftime("%d / %m / %Y") # Aparece a data no formato dd/mm/aaaa
        else:
            formatted_date = "Sem prazo definido"

        responsible_profiles = task.responsible.all()  # Pegando os responsáveis da tarefa
        responsible_photos = []
        
        for resp in responsible_profiles:
            if resp.photo:
                responsible_photos.append(base64.b64encode(resp.photo).decode('utf-8'))
            else:
                responsible_photos.append(None)
        
        pair_r_p = list(zip(task.get_responsibles(), responsible_photos))
        items.append({
            'id': task.id,
            'status': task.status,
            'title': task.title,
            'description': task.description,
            'creation_date': task.creation_date,
            'prazo': formatted_date,  # Agora com o prazo correto para cada task
            'completion_date': task.completion_date,
            'responsible': task.get_responsibles_as_string(),
            'responsible_photos': responsible_photos,
            'responsible_count': task.responsible.count(),
            'pair_responsible_photo': pair_r_p,
        })
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        prazo = request.POST.get('Prazo') or None
        responsible = request.POST.get('responsibles') 
        
        responsible = list(map(int, responsible.split(',')))

        # Cria a instância de Task
        task = Task.objects.create(
            title=title,
            description=description,
            status=status,
            Prazo=prazo,  # Atribuindo o prazo da nova tarefa
        )

        responsible_members = MembroEquipe.objects.filter(id__in=responsible)
        task.responsible.set(responsible_members)
        
        return redirect('kanban')
       
    return render(request, 'kanbam.html', {'items': items, 'profiles': profiles, 'members': members,})



@api_view(['PATCH'])
def update_task_status(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Log os dados recebidos
    print("Dados recebidos:", request.data)

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
    events_obj = Event.objects.all()

    
    for event in events_obj:
        if event.event_date:
            event.day = event.event_date.day  # Acessa diretamente o dia
            event.month = event.event_date.month  # Acessa diretamente o mês
        else:
            # Se a data do evento não estiver presente, atribui valores padrão
            event.day = None
            event.month = None

    # Segunda parte - Calendário e Filtros
    selected_date = request.GET.get('date')
    now = datetime.strptime(selected_date, '%Y-%m-%d') if selected_date else datetime.now()
    
    year, month, day = now.year, now.month, now.day

    weeks = get_calendar_data(year, month, now, request.user)

    # Aplica os filtros de eventos, tarefas e reuniões
    events_filtered = filters(Event, 'event_date', year, month, day)
    tasks = filters(Task, 'creation_date', year, month, day, request.user)
    meetings = filters(Meeting, 'meeting_date', year, month, day).filter(areas__membros=request.user).distinct()

    user_area = request.user.areas.first()
    meetings_data = get_meeting(meetings)

    # Criação do contexto final com todos os dados
    context = {
        "now": now,
        "year": year,
        "month": month,
        "month_name": calendar.month_name[month],
        "weeks": weeks,
        "events": events_filtered,
        "events_obj": events_obj,
        "announcements": announcements,
        "tasks": tasks,
        "meetings": meetings_data,
        "user_area_color": user_area.color if user_area else '#0075F6',
    }

    # Retorna a renderização com o contexto
    return render(request, 'home.html', context)


def get_calendar_data(year, month, now, user):
    cal = calendar.Calendar(firstweekday=6) 
    days = cal.itermonthdays4(year, month) 

    weeks = []
    week = []
    for day in days:
        day_tasks = Task.objects.filter(creation_date__year=day[0], creation_date__month=day[1], creation_date__day=day[2], responsible=user)
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
                "meetings": day_meetings.exists()
            })
        else:
            week.append({
                "day": day[2], 
                "in_month": False, 
                "is_today": False,
                "tasks": day_tasks.exists(),
                "events": day_events.exists(),
                "meetings": day_meetings.exists()
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
            "time": localtime(meeting.meeting_date).strftime('%H:%M'),
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
        year, month, day = selected_date.year, selected_date.month, selected_date.day

        events = filters(Event, 'event_date', year, month, day)
        tasks = filters(Task, 'creation_date', year, month, day, request.user)
        meetings = filters(Meeting, 'meeting_date', year, month, day).filter(areas__membros=request.user).distinct()

        events_data = [{"title": event.title, "time": localtime(event.event_date).strftime('%H:%M')} for event in events]
        tasks_data = [{"title": task.title, "time": localtime(task.creation_date).strftime('%H:%M')} for task in tasks]
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


