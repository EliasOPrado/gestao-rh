# Create your tasks here

# from demoapp.models import Widget

from celery import shared_task
from django.core.mail import send_mail
from apps.funcionarios.models import Funcionario


@shared_task
def send_relatorio():
    total = Funcionario.objects.all().count()
    send_mail(
        'Relatorio Celery',
        'Relatorio geral de funcionarios %f' % total,
        'eliasprado123@outlook.com',
        ['eliaspradoprofessional@outlook.com']
        fail_silently=False
    )
    return True