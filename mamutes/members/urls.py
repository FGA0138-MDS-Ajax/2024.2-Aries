from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ColumnViewSet, TaskViewSet
from . import views
from .views import update_task_status

router = DefaultRouter()
router.register(r'columns', ColumnViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.kanban_view, name='kanban'),
    path('api/tasks/<int:task_id>/update-status/', update_task_status, name='update_task_status'),
    path('profiles/', views.profile_list, name='profile_list'),
]
