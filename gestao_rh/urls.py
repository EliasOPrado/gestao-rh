"""gestao_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("apps.core.urls")),
    # path("departamentos/", include("apps.departamentos.urls")),
    # path("documentos/", include("apps.documentos.urls")),
    # path("empresas/", include("apps.empresas.urls")),
    path("funcionarios/", include("apps.funcionarios.urls")),
    # path("registro-de-horas/", include("apps.registro_de_horas.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path("admin/", admin.site.urls),
]
