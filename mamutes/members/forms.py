from django import forms
from .models import Task, Event, Meeting, Subtask, MembroEquipe, Post
from django.forms.models import inlineformset_factory
from datetime import datetime
class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['description', 'done']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

        posted_at = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'completion_date', 'Prazo', 'responsible', 'has_subtasks', 'vetor_subtasks']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'Titulo-input', 'placeholder': 'Título da tarefa'}),
            'description': forms.Textarea(attrs={'class': 'Descrição-input', 'rows': 5, 'placeholder': 'Descrição detalhada'}),
            'status': forms.Select(attrs={'class': 'option_field'}),
            'completion_date': forms.DateInput(attrs={'class': 'data-input', 'type': 'date'}),
            'Prazo': forms.DateInput(attrs={'class': 'data-input', 'type': 'date'}),
            'responsible': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'vetor_subtasks': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'event_date',
            'location',
            'is_online',
            'event_time',
        ]

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