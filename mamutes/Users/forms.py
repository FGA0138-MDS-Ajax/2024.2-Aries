from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class MembroEquipeCreationForm(UserCreationForm):
    class Meta:
        model = MembroEquipe
        fields = ('username', 'fullname', 'email', 'phone', 'password1', 'password2')

class MembroEquipeChangeForm(UserChangeForm):
    class Meta:
        model = MembroEquipe
        fields = ('username', 'email', 'phone', 'fullname',  )
