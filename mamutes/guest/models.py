from django.db import models

class AdmissionState(models.Model):
    is_open = models.BooleanField(default=True)  # Processo seletivo aberto?
    link_admission = models.URLField(max_length=500, blank=True, null=True)  # Link do formulário

    def __str__(self):
        return "Aberto" if self.is_open else "Fechado"

