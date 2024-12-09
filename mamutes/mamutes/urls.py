from django.contrib import admin
from django.urls import path
from Users.views import login, register, recoverAccount, redefinePassword
from guest.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('account_recovery/', recoverAccount, name = 'recoverAccount'),
    path('redefine_password/<str:username>/<str:token>', redefinePassword, name="redefinePassword"),
    path('', index, name="index"),
]
