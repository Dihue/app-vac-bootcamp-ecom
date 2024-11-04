from django.contrib.auth import views as views_django
from django.urls import path

from . import views

# Nombre de la app para diferenciar a sus propias URLS
app_name = "usuarios"

urlpatterns = [
    path('lista/', views.pagina_usuarios, name='lista'),
    path('nuevo/', views.nuevo, name='nuevo'),
]
