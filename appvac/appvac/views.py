from django.shortcuts import render


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
    """ print("======================")
    print("PARAMETROS GET --> ", request.GET)
    username = request.GET.get("username", default=None)
    password = request.GET.get("password", default=None) """
    
    username = request.POST.get("username", default=None)
    password = request.POST.get("password", default=None)

    print("Username:", username)
    print("Password:", password)

    return render(request,'login.html', {})
