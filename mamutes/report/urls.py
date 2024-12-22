from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_list, name='flight_list'),           # Listar todos os voos
    path('create/', views.flight_create, name='flight_create'), # Criar um novo voo
    path('<int:id>/edit/', views.flight_edit, name='flight_edit'), # Editar um voo
    path('<int:id>/delete/', views.flight_delete, name='flight_delete'), # Deletar um voo
]
