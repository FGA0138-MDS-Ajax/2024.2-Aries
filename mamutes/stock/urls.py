from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock, name='stock'),
    path('adicionar/', views.adicionar_ferramenta, name='adicionar_ferramenta'),  
    path('editar/<int:pk>/', views.editar_ferramenta, name='editar_ferramenta'),  
    path('deletar/<int:pk>/', views.deletar_ferramenta, name='deletar_ferramenta'), 
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('download-csv/', views.download_csv, name='download_csv'),
    path('stock/', views.stock, name='stock'),
]