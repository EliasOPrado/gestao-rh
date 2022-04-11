from django.db import models
from apps.empresas.models import Empresa
from django.urls import reverse_lazy


# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse_lazy('list_departamentos')

    def __str__(self):
        return str(self.nome)
