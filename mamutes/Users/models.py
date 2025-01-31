from django.db import models
from django.contrib.auth.models import AbstractUser

class Area(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#FFFFFF')
    
    def __str__(self):
        return self.name
    

class Function(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class MembroEquipe(AbstractUser):
    class AreaChoices(models.TextChoices):
        SOFTWARE_ENGINEERING = 'SE', 'Engenharia de Software'
        DATA_SCIENCE = 'DS', 'Ciência de Dados'
        DEVOPS = 'DO', 'DevOps'
        UI_UX = 'UX', 'UI/UX Design'


    fullname = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=False, null=False)
    
    areaUsuario = models.CharField(
        max_length=2,
        choices=AreaChoices.choices,
        default=AreaChoices.SOFTWARE_ENGINEERING,
    )
    photo = models.ImageField(upload_to='fotos_membros/', null=True, blank=True, default='fotos_membros/media/fotos_membros/default.png')
    areas = models.ManyToManyField(Area, related_name='membros', blank=True)
    testearea = models.ManyToManyField(Area, related_name='area', blank=True)
    functions = models.ManyToManyField(Function, related_name='membros', blank=True)

    @property
    def first_name_display(self):
        """Retorna apenas o primeiro nome do usuário."""
        return self.fullname.split()[0] if self.fullname else ""

    def __str__(self):
        return self.username
    def get_area_member(self):
        return self.testearea
