from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def sidebar(request):
    return render(request,"partials/_sidebar.html")

@login_required
def home(request):
    return render(request, "home.html")