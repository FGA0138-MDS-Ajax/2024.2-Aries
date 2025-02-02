from django.contrib import admin
from .models import Tool

# Register your models here.

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'code', 'quantity', 'brand', 'observation', 'location', 'being_used')