from django.shortcuts import redirect, render

from .forms import FormPaciente
from .models import Paciente

# Create your views here.
def nuevo(request):
    template_name = 'pacientes/nuevo.html'
    form = FormPaciente()
    message = ""

    # Acceder al POST e inicializar con esos datos
    if request.method == 'POST':
        form = FormPaciente(request.POST)

        if form.is_valid():
            form.save()
            return redirect("pacientes:lista")
        else:
            message = "No se guardó de forma correcta el formulario"

    ctx = {
        "formPaciente": form,
        "message": message
    }
    return render(request,template_name, ctx)


def lista(request):
    # Trae a todos los pacientes de la tabla Pacientes de la DB
    pacientes = Paciente.objects.all()

    # Para solo traer al primer objeto de toda la lista de "pacientes"
    p = Paciente.objects.filter(id=1).first()

    print("|--> TODOS LOS PACIENTES")
    if p is None:
        print("No existe usuario")
    else:
        print(p)
        print(p.nombre)

    ctx = {
        "pacientes": pacientes
    }
    return render(request,'pacientes/lista.html', ctx)
