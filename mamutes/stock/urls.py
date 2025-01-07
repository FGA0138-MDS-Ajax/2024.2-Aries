from django.urls import path
from . import views

urlpatterns = [
    path('', views.stock, name='stock'),
    path('adicionar/', views.adicionar_ferramenta, name='adicionar_ferramenta'),  
    path('editar/<int:pk>/', views.editar_ferramenta, name='editar_ferramenta'),  
    path('deletar/<int:pk>/', views.deletar_ferramenta, name='deletar_ferramenta'), 
]