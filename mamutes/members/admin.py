from django.contrib import admin
from .models import *
from .forms import * 
from django.forms import CheckboxSelectMultiple


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_event', 'event_date', 'location', 'is_online')  
    search_fields = ('title', 'description')  
    list_filter = ('is_event', 'is_online') 

    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'is_event', 'event_date', 'is_online', 'location')
        }),
    )

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        
        if obj and obj.is_online:
            fields.remove('location') 
        elif 'is_event' in request.POST and 'is_online' not in request.POST:
            if 'location' not in fields:
                fields.append('location')
        
        return fields


class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'status', 'get_responsible', 'completion_date')  
    list_filter = ('status', 'responsible')  
    search_fields = ('description',)  

    def get_responsible(self, obj):
        return ", ".join([responsible.username for responsible in obj.responsible.all()])
    get_responsible.short_description = 'Responsável'

    form = TaskForm

    def save_model(self, request, obj, form, change):
        obj.clean()  
        super().save_model(request, obj, form, change)


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('title', 'meeting_date', 'get_areas')  
    list_filter = ('meeting_date',)  
    search_fields = ('title',)  

    def get_areas(self, obj):
        return ", ".join([area.name for area in obj.areas.all()])
    get_areas.short_description = 'Áreas'


admin.site.register(Event, EventAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Meeting, MeetingAdmin)