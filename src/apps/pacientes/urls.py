from django.urls import path

from . import views

app_name = "pacientes"

urlpatterns = [
    # path('lista/', views.pagina_usuarios, name='lista'),
    path('nuevo/', views.nuevo, name='nuevo'),
    path('lista/', views.lista, name='lista')
]
