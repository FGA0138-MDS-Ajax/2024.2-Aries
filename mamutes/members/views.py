from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import TaskForm, EventForm, BaseEventForm
from .models import MembroEquipe, Event, Task, Meeting, BaseEvent
from rest_framework import viewsets
from .models import Column, Task
from .serializers import ColumnSerializer, TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import calendar
from datetime import datetime, timedelta, date
import locale
from django.utils.dateparse import parse_date
from django.utils.timezone import localtime
import base64

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def sidebar(request):
    members = MembroEquipe.objects.all()
    return render(request,"partials/_sidebar.html", {'members':members})


def Top(request):
     return render(request, 'partials/Top.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        base_event_form = BaseEventForm(request.POST)
        
        if base_event_form.is_valid():
            base_event = base_event_form.save(commit=False)
            base_event.member = request.user  
            base_event.save()

            print(f"Base event saved: {base_event}")  

            if base_event.is_event:     
                event_form = EventForm(request.POST)
                event = event_form.save(commit=False)
                event.base_event = base_event

                if event_form.is_valid():
                    
                    event.save()

                    print(f"Event saved: {event}")  

                else:
                    print(f"Event form errors: {event_form.errors}")  
            else:
                event_form = None  
        else:
            
            event_form = None  

    else:
        base_event_form = BaseEventForm()
        event_form = None  
    
    events = Event.objects.all()
    base_events = BaseEvent.objects.all()    

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
            if hasattr(profile.photo, 'open'):  # Caso seja um arquivo (ImageFieldFile)
                with profile.photo.open('rb') as photo_file:
                    photo_data = photo_file.read()
            else:  # Caso já seja um objeto de bytes
                photo_data = profile.photo

            # Codifica os dados da imagem em Base64
            profile.photo_base64 = base64.b64encode(photo_data).decode('utf-8')

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
    # Obtém a data selecionada ou usa a data atual
    selected_date = request.GET.get('date')
    now = datetime.strptime(selected_date, '%Y-%m-%d') if selected_date else datetime.now()

    # Extrai ano, mês e dia
    year, month, day = now.year, now.month, now.day

    # Obtém os dados do calendário
    weeks = get_calendar_data(year, month, now, request.user)

    # Filtra eventos, tarefas e reuniões
    events = filters(Event, 'event_date', year, month, day)
    announcements = BaseEvent.objects.filter(is_event=False)  # Filtra BaseEvent conforme necessário
    events_objects = Event.objects.all()
    tasks = filters(Task, 'creation_date', year, month, day, request.user)
    meetings = filters(Meeting, 'meeting_date', year, month, day).filter(areas__membros=request.user).distinct()

    # Converte as datas dos eventos para obter o dia e mês
    for event in events_objects:
        try:
            event_date = datetime.strptime(event.event_date, "%Y-%m-%d").date()  # Converte a data do evento
            event.dayObj = event_date.day  # Salva o dia do evento
            event.monthObj = event_date.month  # Salva o mês do evento
        except ValueError:
            event.dayObj = None
            event.monthObj = None
    
    # Converte as datas dos base_events para obter o dia e mês

    # Obtém a área do usuário e os dados das reuniões
    user_area = request.user.areas.first()
    meetings_data = get_meeting(meetings)

    # Contexto para renderização
    context = {
        "now": now,
        "year": year,
        "month": month,
        "month_name": calendar.month_name[month],
        "weeks": weeks,
        "events": events,
        "events_objects": events_objects,
        "announcements": announcements,  # Adiciona os base_events ao contexto
        "tasks": tasks,
        "meetings": meetings_data,
        "user_area_color": user_area.color if user_area else '#0075F6',
    }

    return render(request, "home.html", context)

def get_calendar_data(year, month, now, user):
    cal = calendar.Calendar(firstweekday=6) 
    days = cal.itermonthdays4(year, month) 

    weeks = []
    week = []
    for day in days:
        day_tasks = Task.objects.filter(creation_date__year=day[0], creation_date__month=day[1], creation_date__day=day[2], responsible=user)
        day_events = Event.objects.filter(event_date__icontains=f"{day[0]}-{day[1]:02d}-{day[2]:02d}")
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


def filters(model, date_field, year, month, day, user=None):
    if model == Event:
        filters = {
            f"{date_field}__icontains": f"{year}-{month:02d}-{day:02d}",
        }
    else:
        filters = {
            f"{date_field}__year": year,
            f"{date_field}__month": month,
            f"{date_field}__day": day,
        }
    if user:
        filters["responsible"] = user
    return model.objects.filter(**filters)

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


