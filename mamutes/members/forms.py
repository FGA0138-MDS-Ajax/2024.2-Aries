from django import forms
from .models import Task, Event, Meeting, Subtask,MembroEquipe
from django.forms.models import inlineformset_factory

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['description', 'done']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'completion_date', 'Prazo', 'responsible', 'has_subtasks', 'subtasks']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'Titulo-input', 'placeholder': 'Título da tarefa'}),
            'description': forms.Textarea(attrs={'class': 'Descrição-input', 'rows': 5, 'placeholder': 'Descrição detalhada'}),
            'status': forms.Select(attrs={'class': 'option_field'}),
            'completion_date': forms.DateInput(attrs={'class': 'data-input', 'type': 'date'}),
            'Prazo': forms.DateInput(attrs={'class': 'data-input', 'type': 'date'}),
            'responsible': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'subtasks': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'is_event',
            'event_date',
            'location'
        ]
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = [
            'title',
            'description',
            'meeting_date',
            'areas'
        ]
        widgets = {
            'meeting_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'areas': forms.CheckboxSelectMultiple(),
        }