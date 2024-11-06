from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import FormPaciente
from .models import Paciente


class Nuevo(CreateView):
    template_name = 'pacientes/nuevo.html'
    model = Paciente
    form_class = FormPaciente
    success_url = reverse_lazy("pacientes:lista")

    # Función que viene dentro del CreateView y que se la puede personalizar
    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        ctx["titulo"] = "Nuevo paciente"
        return ctx


class Lista(ListView):
    template_name = 'pacientes/lista.html'
    model = Paciente
    context_object_name = "pacientes"
    paginate_by = 2

    def get_queryset(self):
        query = self.model.objects.all()
        nombre = self.request.GET.get('nombre', None)

        if nombre:
            query = query.filter(nombre= nombre)
        
        return query.order_by("apellido")
