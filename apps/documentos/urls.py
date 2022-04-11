from django.urls import include, path

from .views import DocumentoCreate

urlpatterns = [

    # ** will pass the funcionario_id to the view DocumentoCreate. **
    # --- Same as done with django-nested-routers ---
    path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
    # path("editar/<int:pk>/", DocumentoEdit.as_view(), name="update_documento"),
    # path("deletar/<int:pk>/", DocumentoDelete.as_view(), name="delete_documento"),
]
