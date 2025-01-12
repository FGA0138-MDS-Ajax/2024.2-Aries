from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include
from Users.views import login, register, recoverAccount, redefinePassword
<<<<<<< HEAD
from guest.views import index, competition, admission
from members.views import sidebar, home
=======
from guest.views import index, competition, admission, control_admission
from members.views import sidebar, create_task, Top
>>>>>>> 383132100d87c7029e6b4e0984ee6476506ad049

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
<<<<<<< HEAD
    path('sidebar/', sidebar,name="sidebar"),
    path('home/', home, name="home"),

=======
    path('sidebar/', sidebar , name="sidebar"),
    path('create_task/', create_task, name= "create_task"),
    path('Top/', Top, name='top')
>>>>>>> 383132100d87c7029e6b4e0984ee6476506ad049
    # stock
    
]

handler404 = 'guest.views.custom_404_view'
