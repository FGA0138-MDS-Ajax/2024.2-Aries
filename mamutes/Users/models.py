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

    areas = models.ManyToManyField(Area, related_name='membros', blank=True)
    functions = models.ManyToManyField(Function, related_name='membros', blank=True)

    def __str__(self):
        return self.username
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # Chave primária explícita
    CARGOS = [
        ('Admin', 'Administrador'),
        ('Piloto', 'Piloto'),
        ('Trainee', 'Trainee'),
        ('Usuario', 'Usuário'),
    ]
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    papel = models.CharField(max_length=10, choices=CARGOS)

    def __str__(self):
        return self.nome
class Tarefa(models.Model):
    id = models.AutoField(primary_key=True)  
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Progresso', 'Em Progresso'),
        ('Concluída', 'Concluída'),
    ]
    descricao = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank=True)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao} - {self.status}"
class Produto(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    categoria = models.CharField(max_length=50)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Ata(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class RegistroAcidente(models.Model):
    id = models.AutoField(primary_key=True)  
    data = models.DateField()
    nome_equipe_registradora = models.TextField()
    funcao_equipe_registradora = models.TextField()
    membros_envolvidos = models.TextField()
    local_problema = models.TextField()
    explicacao_detalhada = models.TextField()
    codigo_peca_danificada = models.CharField(max_length=50)
    velocidade_m_s = models.DecimalField(max_digits=10, decimal_places=2)
    direcao_vento = models.CharField(max_length=50)
    pressao_atmosferica_hpa = models.DecimalField(max_digits=10, decimal_places=2)
    peso_decolagem_kg = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_voos_piloto = models.IntegerField()
    impressoes_piloto = models.TextField()
    telemetria_link = models.URLField()
    foto_pecas_danificadas_link = models.URLField()

    def __str__(self):
        return f"Acidente - {self.data} - {self.local_problema}"
