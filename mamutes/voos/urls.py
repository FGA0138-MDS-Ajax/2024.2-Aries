from django.urls import path
from . import views

urlpatterns = [
    path('', views.voo_list, name='voo_list'),           # Listar todos os voos
    path('create/', views.voo_create, name='voo_create'), # Criar um novo voo
    path('<int:id>/edit/', views.voo_edit, name='voo_edit'), # Editar um voo
    path('<int:id>/delete/', views.voo_delete, name='voo_delete'), # Deletar um voo
]
