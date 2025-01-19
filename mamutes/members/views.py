from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import TaskForm
from .models import MembroEquipe, Event, Task, Meeting
from django.contrib.auth.decorators import login_required
import calendar
from datetime import datetime, timedelta
import locale
from django.utils.dateparse import parse_date
from django.utils.timezone import localtime

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

def sidebar(request):
    members = MembroEquipe.objects.all()
    return render(request,"partials/_sidebar.html", {'members':members})

def Top(request):
    return render(request, 'partials/Top.html')

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sidebar')   
        else:
            members = MembroEquipe.objects.all()
            return render(request, "partials/_sidebar.html", {'members':members})

    else:
        return redirect('sidebar')

@login_required
def home(request):
    selected_date = request.GET.get('date')
    if selected_date:
        now = datetime.strptime(selected_date, '%Y-%m-%d')
    else:
        now = datetime.now()
    
    year = now.year
    month = now.month

    weeks = get_calendar_data(year, month, now, request.user)

    events = Event.objects.filter(
        event_date__year=year, 
        event_date__month=month,
        event_date__day=now.day)
    tasks = Task.objects.filter(
        creation_date__year=year, 
        creation_date__month=month, 
        creation_date__day=now.day,
        responsible=request.user)
    meetings = Meeting.objects.filter(
        meeting_date__year=year, 
        meeting_date__month=month, 
        meeting_date__day=now.day).filter(areas__membros=request.user).distinct()

    user_area = request.user.areas.first() 
    meetings_data = []
    for meeting in meetings:
        multiple_teams = meeting.areas.count() > 1
        meetings_data.append({
            "title": meeting.title,
            "meeting_date": meeting.meeting_date,
            "multiple_teams": multiple_teams,
        })

    context = {
        "now": now,
        "year": year,
        "month": month,
        "month_name": calendar.month_name[month],
        "weeks": weeks,
        "events": events,
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

def get_events_tasks(request):
    date_str = request.GET.get('date')
    
    if date_str:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d')
        year = selected_date.year
        month = selected_date.month
        day = selected_date.day

        events = Event.objects.filter(
            event_date__year=year, 
            event_date__month=month, 
            event_date__day=day)
        tasks = Task.objects.filter(
            creation_date__year=year, 
            creation_date__month=month, 
            creation_date__day=day, 
            responsible=request.user
        )
        meetings = Meeting.objects.filter(
            meeting_date__year=year, 
            meeting_date__month=month, 
            meeting_date__day=day
        ).filter(areas__membros=request.user).distinct()

        events_data = [{"title": event.title, "time": localtime(event.event_date).strftime('%H:%M')} for event in events]
        tasks_data = [{"title": task.title, "time": localtime(task.creation_date).strftime('%H:%M')} for task in tasks]
        
        meetings_data = []
        for meeting in meetings:
            areas = meeting.areas.all()
            multiple_teams = areas.count() > 1
            meetings_data.append({
                "title": meeting.title,
                "time": localtime(meeting.meeting_date).strftime('%H:%M'),
                "multiple_teams": multiple_teams
            })
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

