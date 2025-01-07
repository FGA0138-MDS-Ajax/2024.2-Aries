from django.contrib import admin
from django.urls import path, include
from Users.views import login, register, recoverAccount, redefinePassword
from guest.views import index, competition, admission, control_admission
from members.views import sidebar, create_task, Top
from stock.views import stock

urlpatterns = [

    path('admin/', admin.site.urls),

    # Users
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('account_recovery/', recoverAccount, name='recoverAccount'),
    path('redefine_password/<str:username>/<str:token>', redefinePassword, name="redefinePassword"),

    # guest
    path('', index, name="index"),
    path('competition/', competition, name="competition"),
    path('admission/', admission, name="admission"),
    path('control_admission/', control_admission, name='control_admission'),

    # report
    path('report/', include('report.urls')),

    # members
    path('sidebar/', sidebar , name="sidebar"),
    path('create_task/', create_task, name= "create_task"),
    path('Top/', Top, name='top'),

    # stock
    path('stock/', stock, name='stock'),
    path('', include('stock.urls')),
]
