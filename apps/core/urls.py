from django.urls import include, path
from .views import home, celery

from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("celery", celery, name="celery"),
]
