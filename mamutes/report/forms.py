from django import forms
from .models import FlightLog

class FlightForm(forms.ModelForm):
    class Meta:
        model = FlightLog
        fields = '__all__'  # Inclui todos os campos do modelo Voo
