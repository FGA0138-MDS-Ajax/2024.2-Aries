from django.shortcuts import render

# Create your views here.


def stock(request):
    return render(request, 'stock.html')