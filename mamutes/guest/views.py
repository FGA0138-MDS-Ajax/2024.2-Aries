from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def competition(request):
    return render(request,'comp.html')
