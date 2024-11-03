from django.shortcuts import render

from .models import Usuario

# Create your views here.
def pagina_usuarios(request):
    # Trae a todos los objetos de la tabla Usuario de la DB
    usuarios = Usuario.objects.all() # filter(id__in=[1,2,3])

    # Trae solo a los objetos, que coinciden con los valores
    # del filter de la tabla Usuario de la DB
    # usuarios = Usuario.objects.filter(id__in=[1,2,3])

    # Para solo traer al primer objeto de toda la lista de "usuarios"
    u = Usuario.objects.filter(id=1).first()

    print("|--> TODOS LOS USUARIOS")
    if u is None:
        print("No existe usuario")
    else:
        print(u)
        print(u.username)
    '''
    print("|--> TODOS LOS USUARIOS")
    print(usuarios)
    print(usuarios.query)
    print("|--> Longitud:", len(usuarios))
    print("|--> Longitud:", usuarios.count())

    # Al tratarse de un QuerySet puedo iterar
    for us in usuarios:
        print(us.last_login)
    '''
    ctx = {
        "usuarios": usuarios
    }
    return render(request,'usuarios/lista.html', ctx)