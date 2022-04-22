from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from apps.funcionarios.models import Funcionario
from .tasks import send_relatorio


def celery(request):
    send_relatorio.delay()
    return HttpResponse("Tarefa incluida na fila para execução.")


@login_required
def home(request):
    data = {}
    data["usuario"] = request.user
    return render(request, "core/index.html", data)
