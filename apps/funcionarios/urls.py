from django.urls import include, path

from .views import (FuncionarioCreate, FuncionariosDelete, FuncionariosEdit,
                    FuncionariosList)

urlpatterns = [
    path("", FuncionariosList.as_view(), name="list_funcionarios"),
    path("novo/", FuncionarioCreate.as_view(), name="create_funcionario"),
    path("editar/<int:pk>/", FuncionariosEdit.as_view(), name="update_funcionario"),
    path("deletar/<int:pk>/", FuncionariosDelete.as_view(), name="delete_funcionario"),
]
