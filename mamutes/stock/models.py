from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    observation = models.TextField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=100)
    being_used = models.BooleanField(default=False)
    def __str__(self):
        return self.name