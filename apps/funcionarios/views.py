import io

from django.contrib.auth.models import User
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from reportlab.pdfgen import canvas

from .models import Funcionario

from django.views.generic.base import View, TemplateView
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa 


# Create your views here.
class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ["nome", "departamento"]

    def form_valid(self, form):

        # avoid send to db.
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = funcionario.nome.split(" ")[0] + funcionario.nome.split(" ")[1]
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


def relatorio_funcionarios(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, "Relatorio de funcionarios")

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = "Nome: %s | Hora Extra: %.2f"

    p.drawString(0, 800, "_" * 150)

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas_extra))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')


class PdfDebug(TemplateView):
    template_name = 'funcionarios/relatorio.html'
