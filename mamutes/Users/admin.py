from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import MembroEquipeCreationForm, MembroEquipeChangeForm
from .models import MembroEquipe, Area, Function, Position

class MembroEquipeAdmin(UserAdmin):
    add_form = MembroEquipeCreationForm
    form = MembroEquipeChangeForm
    model = MembroEquipe

    list_display = ('username', 'fullname', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'fullname', 'phone', 'email','area', 'functions', 'position')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'fullname', 'phone', 'email', 'password1', 'password2','area', 'functions')
        }),
    )

class AreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('listar_membros',)

    def listar_membros(self, obj):
        return ", ".join([membro.id for membro in obj.membros.all()])
    listar_membros.short_description = 'Membros da Área'

class FunctionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    readonly_fields = ('listar_membros',)

    def listar_membros(self, obj):
        return ", ".join([membro.username for membro in obj.membros.all()])
    listar_membros.short_description = 'Membros da Função'

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Position, PositionAdmin)
admin.site.register(MembroEquipe, MembroEquipeAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Function, FunctionAdmin)