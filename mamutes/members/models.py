from django.db import models
from Users.models import MembroEquipe, Area

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
    creation_date = models.DateField(auto_now_add=True)
    completion_date = models.DateField(null=True, blank=True)
    Prazo = models.DateField(null=True, blank=True)
    area = models.ManyToManyField(Area, related_name='areatask', blank=True)
    responsible = models.ManyToManyField(MembroEquipe)
    has_subtasks = models.BooleanField(default=False)
    vetor_subtasks = models.CharField(max_length=500, null=True, blank=True)  
    class PriorityChoices(models.IntegerChoices):
        LOW = 1, 'Baixa Prioridade'
        MEDIUM = 2, 'Média Prioridade'
        HIGH = 3, 'Alta Prioridade'

    priority = models.IntegerField(
        choices=PriorityChoices.choices,
        default=PriorityChoices.LOW,
    )
    def is_complete(self):
        return all(subtask.done for subtask in self.subtasks.all())
    
    def get_responsibles(self):
        """
        Retorna uma lista com os nomes de todos os responsáveis.
        """
        return [responsible.fullname for responsible in self.responsible.all()]
    
    def get_responsiblesPhotos(self):
       
        return [responsible.photo for responsible in self.responsible.all()]

    def get_responsibles_as_string(self):
        """
        Retorna os nomes de todos os responsáveis em uma string formatada.
        """
        return ", ".join(responsible.username for responsible in self.responsible.all())

    def __str__(self):
        return f"{self.description} - {self.status}"


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.description



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
    
    
class Column(models.Model):
    name = models.CharField(max_length=100)

def __str__(self):
    return self.name

class Task1(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name='tasks')
    position = models.PositiveIntegerField(default=0)  # Para ordenar as tarefas

    def __str__(self):
        return self.title