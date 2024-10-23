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
    return render(request,'login.html', {})
