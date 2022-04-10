from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.models import User

from .models import Funcionario


# Create your views here.
class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "departamento"]

    def form_valid(self, form):
        
        # avoid send to db.
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)
class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset


class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields = ["nome", "departamento"]


class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy("list_funcionarios")
