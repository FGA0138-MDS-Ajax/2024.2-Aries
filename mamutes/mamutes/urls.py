from django.contrib import admin
from django.urls import path
from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('login/', views.login, name = 'login'),
    path('cadastro/', views.cadastro, name = 'cadastro'),
    path('recuperarConta/', views.recuperarConta, name = 'recuperarConta'),
]
