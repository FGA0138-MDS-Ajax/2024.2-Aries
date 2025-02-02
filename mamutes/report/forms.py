from django import forms


from .models import FlightLog,Meeting,Area

class FlightForm(forms.ModelForm):
    class Meta:
        model = FlightLog
        fields = '__all__'  # Inclui todos os campos do modelo Voo
class MeetingsForm(forms.ModelForm):
    areas = forms.ModelMultipleChoiceField(
        queryset=Area.objects.all(),
        widget=forms.CheckboxSelectMultiple(),  # O widget padrão será sobrescrito no HTML
        required=False
    )

    class Meta:
        model = Meeting
        fields = '__all__'