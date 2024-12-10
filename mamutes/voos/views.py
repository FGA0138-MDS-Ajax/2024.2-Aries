from django.shortcuts import render, redirect, get_object_or_404
from .models import Voo
from .forms import VooForm

# Listar todos os voos
def voo_list(request):
    voos = Voo.objects.all()
    return render(request, 'voos/voo_list.html', {'voos': voos})

# Criar um novo voo
def voo_create(request):
    if request.method == 'POST':
        form = VooForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voo_list')
    else:
        form = VooForm()
    return render(request, 'voos/voo_form.html', {'form': form})

# Editar um voo existente
def voo_edit(request, id):
    voo = get_object_or_404(Voo, id=id)
    if request.method == 'POST':
        form = VooForm(request.POST, instance=voo)
        if form.is_valid():
            form.save()
            return redirect('voo_list')
    else:
        form = VooForm(instance=voo)
    return render(request, 'voos/voo_form.html', {'form': form})

# Deletar um voo
def voo_delete(request, id):
    voo = get_object_or_404(Voo, id=id)
    if request.method == 'POST':
        voo.delete()
        return redirect('voo_list')
    return render(request, 'voos/voo_confirm_delete.html', {'voo': voo})
