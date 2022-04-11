from django.shortcuts import render
from .models import Documento
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertencente_id = self.kwargs['funcionario_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)