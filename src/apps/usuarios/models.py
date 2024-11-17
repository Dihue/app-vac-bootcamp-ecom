from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    dni = models.IntegerField(null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    es_admin = models.BooleanField(default=False)

    # Redefinición del método string
    def __str__(self):
        return f"{self.first_name} {self.last_name}"