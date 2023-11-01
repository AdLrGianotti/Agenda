from django.db import models

# Create your models here.

class Agenda(models.Model):
    Nome = models.CharField(max_length=100)
    Apelido = models.CharField(max_length=30)
    Email = models.EmailField(max_length=100)
    DataNascimento = models.DateField
    Endereco = models.CharField(max_length=200)
    Numero = models.CharField(max_length=10)
    Complemento = models.CharField(max_length=50)
    Cep = models.CharField(max_length=9)
    Bairro = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    Estado = models.CharField(max_length=50)
     