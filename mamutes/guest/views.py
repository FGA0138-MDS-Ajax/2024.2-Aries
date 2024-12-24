from django.shortcuts import render, redirect
from .models import AdmissionState

def index(request):
    return render(request, 'index.html')

def competition(request):
    return render(request, 'comp.html')

def admission(request):
    state = AdmissionState.objects.first()
    if not state:
        state = AdmissionState.objects.create(is_open=True)
    return render(request, 'admission.html', {'state': state})

def control_admission(request):
    state = AdmissionState.objects.first()
    if not state:
        state = AdmissionState.objects.create(is_open=True)
    
    if request.method == 'POST':
        state.is_open = not state.is_open
        state.save()
        return redirect('control_admission')
    
    return render(request, 'control_admission.html', {'state': state})
