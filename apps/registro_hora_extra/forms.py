from django.forms import ModelForm

from apps.funcionarios.models import Funcionario

from .models import RegistroHoraExtra


class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        # ** set funcionario as the logged user. (filter) **
        self.fields["funcionario"].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa
        )

    class Meta:
        model = RegistroHoraExtra
        fields = ["motivo", "funcionario", "horas"]
