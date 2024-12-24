from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def competition(request):
    return render(request,'comp.html')

def admission(request):
    return render(request,'admission.html')

def handler404(request, exception):
    return render(request, 'error404.html')

