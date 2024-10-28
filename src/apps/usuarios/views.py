from django.shortcuts import render

# Create your views here.
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