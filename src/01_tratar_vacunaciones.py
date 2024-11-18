# Script para tratar con el ORM de manera directa
# En consola ejecutar: python 01_tratar_vacunaciones.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.colocacion.models import ColocacionVacuna

archivo = open("vacunaciones.csv", "w")

# Cabezeras
archivo.write(f"apellido y nombre;fecha;nombre vacuna;dosis\n")

for vac in ColocacionVacuna.objects.all():
    archivo.write(f"{vac.paciente};{vac.fecha_aplicacion};{vac.dosis.vacuna};{vac.dosis.nombre}\n")
    print("--> Vacuna:", vac)

archivo.close()