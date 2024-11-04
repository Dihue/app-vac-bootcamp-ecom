from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    dni = models.IntegerField(null=True)

    # Redefinición del método string
    def __str__(self):
        return f"ID: {self.id} - Username: {self.username} - {self.first_name}"