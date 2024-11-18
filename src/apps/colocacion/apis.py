from rest_framework import generics

from .models import ColocacionVacuna
from .serializers import VacunacionSerializer


class VacunacionesCrearYListar(generics.ListCreateAPIView):
    queryset = ColocacionVacuna.objects.all()
    serializer_class = VacunacionSerializer