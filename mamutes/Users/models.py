from django.db import models
from django.contrib.auth.models import AbstractUser

class Area(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Function(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class MembroEquipe(AbstractUser):
    fullname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)

    #areas = models.ManyToManyField(Area, related_name='membros', blank=True)
    #functions = models.ManyToManyField(Function, related_name='membros', blank=True)

    def __str__(self):
        return self.username
