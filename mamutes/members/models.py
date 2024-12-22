from django.db import models
from Users.models import MembroEquipe

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)  
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Progresso', 'Em Progresso'),
        ('Concluída', 'Concluída'),
    ]
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    creation_date = models.DateTimeField(auto_now_add=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    responsible = models.ForeignKey(MembroEquipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - {self.status}"
