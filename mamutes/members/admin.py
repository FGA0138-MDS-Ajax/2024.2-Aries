from django.contrib import admin
from .models import *
from .forms import * 
from django.forms import CheckboxSelectMultiple

@admin.register(Task)
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


from django.contrib import admin
from .models import Post, Event

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "member", "is_event", "posted_at", "time_since_posted")
    list_filter = ("is_event", "posted_at")
    search_fields = ("title", "description", "member__name")
    ordering = ("-posted_at",)

    def time_since_posted(self, obj):
        return obj.time_since_posted()
    time_since_posted.short_description = "Tempo desde postagem"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "member", "event_date", "event_time", "location", "is_online")
    list_filter = ("event_date", "is_online")
    search_fields = ("title", "description", "location", "member__name")
    ordering = ("-event_date",)

# admin.site.register(Task1)
# admin.site.register(Column)