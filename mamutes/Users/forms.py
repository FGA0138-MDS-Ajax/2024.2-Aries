from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MembroEquipe, Area, Function

class MembroEquipeCreationForm(UserCreationForm):
    areas = forms.ModelMultipleChoiceField(
        queryset=Area.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    functions = forms.ModelMultipleChoiceField(
        queryset=Function.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = MembroEquipe
        fields = ('username', 'fullname', 'email', 'phone', 'password1', 'password2', 'areas', 'functions')

class MembroEquipeChangeForm(UserChangeForm):
    areas = forms.ModelMultipleChoiceField(
        queryset=Area.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    functions = forms.ModelMultipleChoiceField(
        queryset=Function.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = MembroEquipe
        fields = ('username', 'email', 'phone', 'fullname', 'areas', 'functions')
