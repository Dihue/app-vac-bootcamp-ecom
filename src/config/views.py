from django.contrib.auth import authenticate, login as login_django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from apps.util.decorators import verificar_permisos


class BaseTemplateView(TemplateView):
    template_name = "blank.html"


#@verificar_permisos()
def mi_pagina_inicio(request):

    ctx = {
        "TITULO": "INICIO"
    }

    return render(request,'mi_pagina_inicio.html', ctx)


def login(request):
    # Recuperación de datos mediante el método GET
    """
    print("PARAMETROS GET --> ", request.GET)
    username = request.GET.get("username", default=None)
    password = request.GET.get("password", default=None)
    """
    # Variables de control
    se_autentico = False
    algo_salio_mal = True
    username = ""

    # Recuperación de datos mediante el método POST
    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)

        # Permite identificar si el usuario está en la DB
        usuario = authenticate(request, username=username, password=password)
        se_autentico = True

        # Verificación del login del usuario
        if usuario:
            algo_salio_mal = False
            login_django(request, usuario)
            return redirect("inicio")
        else:
            print("|---> Autenticación MAL")
    
    ctx = {
        "se_autentico": se_autentico,
        "algo_salio_mal": algo_salio_mal,
        "username": username
    }

    return render(request,'login.html', ctx)


def pagina_error_permisos(request):
    template_name = 'decoradores/error_permisos.html'
    ctx = {}

    return render(request, template_name, ctx)