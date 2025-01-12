from django.db import models

class AdmissionState(models.Model):
    is_open = models.BooleanField(default=True)  # processo seletivo aberto?
    
    def __str__(self):
        return self.is_open
