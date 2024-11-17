import datetime

from django.db import models

from apps.pacientes.models import Paciente
from apps.vacunas.models import Dosis

class ColocacionVacuna(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    dosis = models.ForeignKey(Dosis, on_delete=models.CASCADE)
    fecha_aplicacion = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return f"{self.paciente} - {self.dosis.vacuna} - {self.dosis}"
