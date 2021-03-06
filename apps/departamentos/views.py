from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Departamento


# Create your views here.
class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ["descricao", "pertencente"]

    def form_valid(self, form):
        # avoid send to db.
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)


class DepartamentoList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_logada)
        return queryset


class DepartamentoEdit(UpdateView):
    model = Departamento
    fields = ["nome"]


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy("list_departamentos")
