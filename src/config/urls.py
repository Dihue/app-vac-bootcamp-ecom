"""
URL configuration for appvac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth import views as views_django
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mi_pagina_inicio, name='inicio'),

    # path('login/', views.login, name='login'),
    # *Uso de libreria django y vista basada en clase
    path('login/', views_django.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', views_django.logout_then_login, name="logout"),

    path('usuarios/lista/', views.pagina_usuarios, name='lista_de_usuarios'),
    path('pacientes/lista', views.pagina_pacientes, name='lista_de_pacientes')
]
