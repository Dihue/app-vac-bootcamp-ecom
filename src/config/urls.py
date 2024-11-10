from django.contrib import admin
from django.contrib.auth import views as views_django
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mi_pagina_inicio, name='inicio'),

    # path('login/', views.login, name='login'),
    # *Uso de libreria django y vista basada en clase
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', views_django.logout_then_login, name="logout"),

    # path('usuarios/lista/', views.pagina_usuarios, name='lista_de_usuarios'),
    path('usuarios/', include("apps.usuarios.urls")),
    path("pacientes/", include("apps.pacientes.urls")),
    path("vacunas/", include("apps.vacunas.urls"))
]