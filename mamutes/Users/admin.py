from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MembroEquipeCreationForm, MembroEquipeChangeForm
from .models import MembroEquipe, Area, Function

class MembroEquipeAdmin(UserAdmin):
    add_form = MembroEquipeCreationForm
    form = MembroEquipeChangeForm
    model = MembroEquipe

    list_display = ('username', 'fullname', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'fullname', 'phone', 'email', 'areas', 'functions')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'fullname', 'phone', 'email', 'password1', 'password2', 'areas', 'functions')
        }),
    )

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('listar_membros',)

    def listar_membros(self, obj):
        return ", ".join([membro.username for membro in obj.membros.all()])
    listar_membros.short_description = 'Membros da Área'

class FunctionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('listar_membros',)

    def listar_membros(self, obj):
        return ", ".join([membro.username for membro in obj.membros.all()])
    listar_membros.short_description = 'Membros da Função'

admin.site.register(MembroEquipe, MembroEquipeAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Function, FunctionAdmin)