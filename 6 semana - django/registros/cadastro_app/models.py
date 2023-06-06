from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=20)
    nascimento = models.DateField(null=True, blank=True)
    cidade = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, default="email")