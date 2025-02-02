from django.shortcuts import render, redirect
from .models import AdmissionState

def index(request):
    state = AdmissionState.objects.first()
    if not state:
        state = AdmissionState.objects.create(is_open=True)
    return render(request, 'index.html', {'state':state})

def competition(request):
    return render(request, 'comp.html')

def admission(request):
    state = AdmissionState.objects.first()
    if not state:
        state = AdmissionState.objects.create(is_open=True)
    return render(request, 'admission.html', {'state': state})

def custom_404_view(request, exception):
    return render(request, 'error404.html', status=404)


