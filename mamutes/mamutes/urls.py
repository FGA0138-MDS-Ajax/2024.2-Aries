from django.contrib import admin
from django.urls import path
from Users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('account_recovery/', views.recoverAccount, name = 'recoverAccount'),
    path('redefine_password/<str:username>/<str:token>', views.redefinePassword, name="redefinePassword"),
    path ('pagConfig/',views.pagConfig,name = 'pagConfig'),
]
