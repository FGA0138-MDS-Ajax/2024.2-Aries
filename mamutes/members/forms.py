from django import forms
from .models import Task, Event, Meeting, Subtask
from django.forms.models import inlineformset_factory

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['description', 'done']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'responsible', 'subtasks']

    subtasks = forms.ModelMultipleChoiceField(
        queryset=Subtask.objects.all(),
        required=False,  
        widget=forms.CheckboxSelectMultiple,
        label="Subtarefas"
    )


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