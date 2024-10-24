from django.db import models

# Create your models here.
class Usuario(models.Model):
    dni = models.IntegerField()
    cuil = models.IntegerField()


class Vacuna(models.Model):
    nombre = models.CharField()

    class Meta:
        db_table = 'vacunas'