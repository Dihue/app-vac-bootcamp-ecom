import django_filters

from .models import Usuario


class UsuarioFiltro(django_filters.FilterSet):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name']