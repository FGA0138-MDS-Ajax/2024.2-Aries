from django import forms
from .models import Voo

class VooForm(forms.ModelForm):
    class Meta:
        model = Voo
        fields = '__all__'  # Inclui todos os campos do modelo Voo
