from django.db import models

# Create your models here.

class Tool(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    quantity = models.IntegerField()
    observation = models.TextField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=100)
    being_used = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    