from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as login_django


def mi_pagina_inicio(request):
    return render(request,'mi_pagina_inicio.html', {})


def pagina_usuarios(request):
    lista_usuarios = [
        {"nombre": "Lucas", "apellido": "Ibañez"},
        {"nombre": "Federico", "apellido": "Aguirre"},
        {"nombre": "Dihue", "apellido": "De Cuadra"},
    ]

    contexto = {
        "todos_los_usuarios": lista_usuarios
    }

    return render(request,'lista_usuarios.html', contexto)


def pagina_pacientes(request):
    return render(request,'lista_pacientes.html', {})


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
