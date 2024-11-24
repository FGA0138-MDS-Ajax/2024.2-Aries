from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *
from .models import *

class MembroEquipeAdmin(UserAdmin):
    add_form = MembroEquipeCreationForm  # Use o formulário de criação personalizado
    form = MembroEquipeChangeForm        # Formulário de alteração personalizado
    model = MembroEquipe

    list_display = ('username', 'fullname', 'email')  ## Lista principal na aba users
    search_fields = ('username', 'email')  
    ordering = ('username',)

    ## O que aparece quando edita um usuario
    fieldsets = (
        (None, {'fields': ('username', 'fullname', 'phone', 'email')}),
    )

    ## O que aparece quando adiciona um usuario
    add_fieldsets = (
        (None, {
            'fields': ('username', 'fullname', 'phone', 'email', 'password1', 'password2')
        }),
    )

admin.site.register(MembroEquipe, MembroEquipeAdmin)
