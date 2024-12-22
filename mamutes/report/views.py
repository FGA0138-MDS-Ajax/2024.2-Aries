from django.shortcuts import render, redirect, get_object_or_404
from .models import FlightLog
from .forms import FlightForm

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
