from django.contrib import admin
from .models import AdmissionState

@admin.register(AdmissionState)
class AdmissionStateAdmin(admin.ModelAdmin):
    list_display = ('is_open', 'link_admission')
    search_fields = ('link_admission',)
