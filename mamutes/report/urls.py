from django.urls import path
from . import views
from .views import membros_por_area, delete_meeting

urlpatterns = [
    path('meetingsquadro/', views.meetings, name='meetingsquadro'), # Listar todas as reuniões
    path('', views.flight_list, name='flight_list'),          # Listar todos os voos
    path('create/', views.flight_create, name='flight_create'), # Criar um novo voo
    path('<int:id>/edit/', views.flight_edit, name='flight_edit'), # Editar um voo
    path('delete/<int:id>/', views.flight_delete, name='flight_delete'), # Deletar um voo
    path('api/membros/<int:area_id>/', membros_por_area, name='membros_por_area'),
    path('delete_meeting/<int:meeting_id>/', delete_meeting, name='delete_meeting'),
]