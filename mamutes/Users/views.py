from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_django
from .models import * 
from .forms import *

def login (request):
    if request.method ==  'GET':
        return render (request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user is not None:
            login_django (request, user)
            return render(request, 'login.html')
            
        else:
            return HttpResponse("Credenciais inválidas.")

