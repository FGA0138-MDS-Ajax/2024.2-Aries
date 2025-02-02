from django.contrib import admin
from .models import  FlightLog
from .models import  Minutes
from .models import  AccidentLog
from .models import  Meeting
# Register your models here.
admin.site.register(FlightLog)
admin.site.register(Minutes)
admin.site.register(AccidentLog)
admin.site.register(Meeting)