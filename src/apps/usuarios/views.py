from django.shortcuts import redirect, render

from .forms import FormUsuario, FormUser
from .models import Usuario

# Create your views here.
def nuevo(request):
    template_name = 'usuarios/nuevo.html'
    # form = FormUsuario()
    form = FormUser()
    message = None

    # Acceder al POST e inicializar con esos datos
    if request.method == 'POST':
        # form = FormUsuario(request.POST)
        form = FormUser(request.POST)

        if form.is_valid():
            form.save()
            return redirect("usuarios:lista")
        else:
            message = "No se guardó de forma correcta el formulario"

    ctx = {
        "formUsuario": form,
        "message": message
    }
    return render(request,template_name, ctx)


def pagina_usuarios(request):
    # Trae a todos los objetos de la tabla Usuario de la DB
    usuarios = Usuario.objects.all()

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
        "usuarios": usuarios,
        "titulo": "Usuarios"
    }
    return render(request,'usuarios/lista.html', ctx)