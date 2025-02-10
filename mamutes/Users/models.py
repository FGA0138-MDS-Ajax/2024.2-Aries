from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class Area(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#FFFFFF')
    
    def __str__(self):
        return self.name
    

class Position(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Function(models.Model):
    name = models.CharField(max_length=100)
    priority_value = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
class MembroEquipe(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    photo = models.ImageField(upload_to='fotos_membros/', null=True, blank=True, default='fotos_membros/media/fotos_membros/default.png')
    areas = models.ManyToManyField(Area, related_name='membros', blank=True)
    area = models.ManyToManyField(Area, related_name='area', blank=True)
    functions = models.ManyToManyField(Function, related_name='membros', blank=True)
    @property
    def first_name_display(self):
        """Retorna apenas o primeiro nome do usuário."""
        return self.fullname.split()[0] if self.fullname else ""

    def __str__(self):
        return self.username
