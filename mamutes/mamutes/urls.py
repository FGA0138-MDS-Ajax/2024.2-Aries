from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include
from Users.views import login, register, recoverAccount, redefinePassword
from guest.views import index, competition, admission, control_admission
from members.views import sidebar, create_task, Top, home, get_events_tasks, previous_month, next_month

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
    path('home/', home, name="home"),
    path('get-events-tasks/', get_events_tasks, name='get_events_tasks'),
    path('previous-month/', previous_month, name='previous_month'),
    path('next-month/', next_month, name='next_month'),
    
    # stock
    
]

handler404 = 'guest.views.custom_404_view'
