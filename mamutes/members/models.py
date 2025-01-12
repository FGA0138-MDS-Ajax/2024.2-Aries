from django.db import models
from Users.models import MembroEquipe, Area

class Subtask(models.Model):
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.description


class BaseEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_event = models.BooleanField(default=False)  

    class Meta:
        abstract = True


class Event(BaseEvent):
    event_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    is_online = models.BooleanField(default=False) 


    def __str__(self):
        return f"{self.title} - {'Online' if not self.location else self.location}"


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Progresso', 'Em Progresso'),
        ('Concluída', 'Concluída'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    responsible = models.ManyToManyField(MembroEquipe)
    has_subtasks = models.BooleanField(default=False)  
    subtasks = models.ManyToManyField(Subtask, related_name='tasks', blank=True)  # Relacionamento de muitos para muitos com Subtask

    def is_complete(self):
        return all(subtask.done for subtask in self.subtasks.all())

    def __str__(self):
        return f"{self.description} - {self.status}"


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    meeting_date = models.DateTimeField()
    areas = models.ManyToManyField(Area)  

    def get_participants(self):
        participants = MembroEquipe.objects.none()
        for area in self.areas.all():
            participants = participants | area.membroequipe_set.all()
        return participants.distinct()

    def __str__(self):
        return f"Reunião: {self.title} - {self.meeting_date.strftime('%d/%m/%Y %H:%M')} - Áreas: {', '.join([area.name for area in self.areas.all()])}"