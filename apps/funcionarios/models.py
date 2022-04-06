from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)