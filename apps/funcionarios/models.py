from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.urls import reverse


# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True
    )

    def get_absolute_url(self):
        return reverse("list_funcionarios")

    @property
    def total_hora_extra(self):
        # query result: {'horas__sum': Decimal('25')}
        total = self.registrohoraextra_set.all().aggregate(
            Sum('horas'))['horas__sum']
        return total


    def __str__(self):
        return str(self.nome)
