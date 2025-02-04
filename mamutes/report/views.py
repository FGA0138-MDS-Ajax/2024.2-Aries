from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import FlightLog,Meeting,Area
from .forms import FlightForm,MeetingsForm
from django.contrib.auth.decorators import login_required

# Listar todos os voos
def flight_list(request):
    flight = FlightLog.objects.all()
    return render(request, 'report/flight_list.html', {'flights': flight})

# Criar um novo voo
def flight_create(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'report/flight_form.html', {'form': form})

# Editar um voo existente
def flight_edit(request, id):
    flight = get_object_or_404(FlightLog, id=id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'report/flight_form.html', {'form': form})

# Deletar um voo
def flight_delete(request, id):
    flight = get_object_or_404(FlightLog, id=id)
    if request.method == 'POST':
        flight.delete()
        return redirect('flight_list')
    return render(request, 'report/flight_confirm_delete.html', {'flight': FlightLog})

@login_required
def meetings(request):
    meetings = Meeting.objects.all() 
    if request.method == 'POST':
        post_data = request.POST.copy()  # Cria uma cópia dos dados para modificar
        post_data.setlist("areas", request.POST.get("areas", "").split(","))  # Converte para lista

        form = MeetingsForm(post_data)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('meetingsquadro')
    
    else:
        form = MeetingsForm()
    areas = Area.objects.all() 
    return render(request, 'meetings.html',{'form': form,'meetings': meetings,"areas": areas})

def flights(request):
    return render(request, 'flights.html')

def membros_por_area(request, area_id):
    """Retorna os membros de uma determinada área."""
    area = get_object_or_404(Area, id=area_id)
    membros = area.membros.all()  # Pega todos os membros que pertencem a essa área
    print("membros:  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(membros)
    membros_data = [
        {
            "id": membro.id,
            "fullname": membro.fullname,
            "email": membro.email,
            "phone": membro.phone,
            "photo": membro.photo.url if membro.photo else None,
        }
        for membro in membros
    ]

    return JsonResponse({"membros": membros_data})

def delete_meeting(request, meeting_id):
    if request.method == "POST":
        meeting = get_object_or_404(Meeting, id=meeting_id)
        meeting.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)