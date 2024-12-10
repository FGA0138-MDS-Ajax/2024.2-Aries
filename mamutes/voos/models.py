from django.db import models
#from Users.models import Usuario


class Voo(models.Model):
    id = models.AutoField(primary_key=True)  
    data = models.DateField()
    nome_piloto = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    membros_envolvidos = models.TextField()
    nivel_sucesso = models.PositiveSmallIntegerField()  # 1 a 5
    descricao_objetivo = models.TextField()
    exito = models.TextField()
    impressoes_piloto = models.TextField()
    melhorias = models.TextField()
    velocidade_m_s = models.DecimalField(max_digits=10, decimal_places=2)
    direcao_vento = models.CharField(max_length=50)
    pressao_atmosferica_hpa = models.DecimalField(max_digits=10, decimal_places=2)
    peso_decolagem_kg = models.DecimalField(max_digits=10, decimal_places=2)
    ciclos_voo = models.IntegerField()
    telemetria_link = models.URLField()

    def __str__(self):
        return f"{self.id} - {self.data} - {self.local}"
