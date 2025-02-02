from django.shortcuts import render, redirect, get_object_or_404
from .models import Tool
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import csv
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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
    return render(request, 'additem.html', {'title': 'Adicionar Ferramenta'})

# Editar ferramenta
def editar_ferramenta(request, pk):
    ferramenta = get_object_or_404(Tool, pk=pk)

    if request.method == 'POST':
      
        ferramenta.name = request.POST.get('name')
        ferramenta.type = request.POST.get('type')
        ferramenta.code = request.POST.get('code')
        ferramenta.brand = request.POST.get('brand')
        ferramenta.quantity = request.POST.get('quantity')
        ferramenta.observation = request.POST.get('observation')
        ferramenta.location = request.POST.get('location')
        ferramenta.being_used = request.POST.get('being_used') == 'on'
        ferramenta.save()

        # os ajustes foram feitos aqui
        return redirect('stock')
    return redirect('stock')

# Deletar ferramenta novo funcional com modal
def deletar_ferramenta(request, pk):
    ferramenta = get_object_or_404(Tool, pk=pk)
    if request.method == "POST":
        ferramenta.delete() 
        return redirect('stock')  
    return redirect('stock') 

# Download PDF
def download_pdf(request):
    # Configurar a resposta como PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ferramentas_customizadas.pdf"'

    # Criar o canvas para desenhar no PDF
    c = canvas.Canvas(response, pagesize=letter)

    # Adicionar imagem
    # c.drawImage("static/img/logo.png", 50, 750, width=100, height=50)

    # Título do PDF
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Relatório de Ferramentas")
    c.setFont("Helvetica", 12)
    c.drawString(50, 720, "Lista de Ferramentas no Estoque:")
    
    # Buscar as ferramentas do banco de dados
    ferramentas = Tool.objects.all()

    # Criar tabela para os dados
    data = [["Nome", "Código", "Tipo", "Marca", "Quantidade", "Local"]]  # Cabeçalho
    for ferramenta in ferramentas:
        data.append([
            ferramenta.name, 
            ferramenta.code, 
            ferramenta.type, 
            ferramenta.brand, 
            ferramenta.quantity, 
            ferramenta.location
        ])

    # Configurar estilo da tabela
    table = Table(data, colWidths=[100, 60, 80, 100, 80, 100])
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # Cabeçalho com fundo azul claro
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Texto do cabeçalho branco
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centralizar texto
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte do cabeçalho
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaçamento do cabeçalho
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Fundo das linhas
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)  # Linhas de grade
    ])
    table.setStyle(style)

    # Colocar tabela no PDF
    table.wrapOn(c, 50, 500)
    table.drawOn(c, 50, 500)

    # Finalizar o PDF
    c.showPage()
    c.save()
    return response

# Download CSV
def download_csv(request):
    # Configurar a resposta como CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ferramentas.csv"'

    # Criar o escritor CSV
    writer = csv.writer(response)
    writer.writerow(['Nome', 'Código', 'Tipo', 'Marca', 'Quantidade', 'Local', 'Observação', 'Em uso'])

    # Buscar as ferramentas no banco
    ferramentas = Tool.objects.all()

    # Adicionar dados no CSV
    for ferramenta in ferramentas:
        writer.writerow([
            ferramenta.name,
            ferramenta.code,
            ferramenta.type,
            ferramenta.brand,
            ferramenta.quantity,
            ferramenta.location,
            ferramenta.observation,
            "Sim" if ferramenta.being_used else "Não"
        ])

    return response


@login_required
# Buscador
def stock(request):
    query = request.GET.get('search', '').strip()  # Obter e limpar o termo de busca
    ferramentas = Tool.objects.all()  # Recuperar todas as ferramentas por padrão

    ferramentasPaginator = Paginator(ferramentas, 20)
    pageNum = request.GET.get('page')
    page = ferramentasPaginator.get_page(pageNum)

    
    if query:  # Filtrar apenas se a busca não estiver vazia
        page = ferramentas.filter(
            Q(name__icontains=query) |
            Q(type__icontains=query) |
            Q(code__icontains=query)
        )

    return render(request, 'stock.html', {'page': page, 'query': query})
