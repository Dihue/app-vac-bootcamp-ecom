from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django_filters.views import FilterView

from .models import Vacuna, Dosis
from .forms import FormVacuna
from .filters import VacunaFiltro

class Listar(LoginRequiredMixin, FilterView):
    template_name = 'vacunas/lista.html'
    model = Vacuna
    context_object_name = 'vacunas'
    paginate_by = 3
    filterset_class = VacunaFiltro

    def get_context_data(self, **kwargs):
        ctx = super(Listar, self).get_context_data(**kwargs)
        ctx["titulo"] = "Lista de vacunas"
        return ctx


class Nuevo(CreateView):
    template_name = 'vacunas/nuevo.html'
    model = Vacuna
    form_class = FormVacuna
    success_url = reverse_lazy("vacunas:lista")

    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        ctx["titulo"] = "Nueva vacuna"
        return ctx


class VacunaUpdate(UpdateView):
    model = Vacuna
    fields = ['codigo', 'nombre', 'cant_dosis']
    template_name = 'vacunas/editar.html'
    success_url = reverse_lazy('vacunas:lista')

    def get_context_data(self, **kwargs):
        ctx = super(VacunaUpdate, self).get_context_data(**kwargs)
        ctx["titulo"] = "Editar vacuna"
        return ctx


class VacunaDetail(DetailView):
    model = Vacuna
    template_name = 'vacunas/detalle.html'
    context_object_name = 'vacuna'
    # Cambiar el pk por otro campo que se necesite usar
    pk_url_kwarg = "id_vacuna"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['dosis'] = Dosis.objects.filter(vacuna=self.object)
        return ctx


class VacunaDeleteView(DeleteView):
    model = Vacuna
    template_name = 'vacunas/confirmar_eliminacion.html'
    success_url = reverse_lazy('vacunas:lista')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['dosis'] = Dosis.objects.filter(vacuna=self.object)
        return ctx