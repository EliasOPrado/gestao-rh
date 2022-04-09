from django.shortcuts import render
from django.views.generic.edit import CreateView
from apps.empresas.models import Empresa

# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', ]
    