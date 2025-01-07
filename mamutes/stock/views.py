from django.shortcuts import render, redirect, get_object_or_404
from .models import Tool

# Create your views here.

def stock(request):
    ferramentas = Tool.objects.all()
    return render(request, 'stock.html', {'ferramentas': ferramentas})

# Adicionar ferramenta
def adicionar_ferramenta(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        code= request.POST.get('code')
        brand = request.POST.get('brand')
        quantity = request.POST.get('quantity')
        observation = request.POST.get('observation')
        location = request.POST.get('location')
        being_used = request.POST.get('being_used') == 'on'
        
        Tool.objects.create(
            name=name,
            type=type,
            code=code,
            brand=brand,
            quantity=quantity,
            observation=observation,
            location=location,
            being_used=being_used
        )
        return redirect('stock')
    return render(request, 'form.html', {'title': 'Adicionar Ferramenta'})

# Editar ferramenta
def editar_ferramenta(request, pk):
    ferramenta = get_object_or_404(Tool, pk=pk)
    if request.method == 'POST':
        ferramenta.name = request.POST.get('name')
        ferramenta.type= request.POST.get('type')
        ferramenta.code= request.POST.get('code')
        ferramenta.brand = request.POST.get('brand')
        ferramenta.quantity = request.POST.get('quantity')
        ferramenta.observation = request.POST.get('observation')
        ferramenta.location = request.POST.get('location')
        ferramenta.being_used = request.POST.get('being_used') == 'on'
        ferramenta.save()
        return redirect('stock')
    return render(request, 'form.html', {'ferramenta': ferramenta, 'title': 'Editar Ferramenta'})

# Deletar ferramenta
def deletar_ferramenta(request, pk):
    ferramenta = get_object_or_404(Tool, pk=pk)
    if request.method == 'POST':
        ferramenta.delete()
        return redirect('stock')
    return render(request, 'confirm_delete.html', {'ferramenta': ferramenta})
