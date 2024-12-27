from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import TaskForm
from .models import MembroEquipe

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