from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

# Crea un formulario a partir del modelo del usuario
# por lo que trae cada campo que ya tiene
class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            "password",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "dni"
        ]


# Hereda de un formulario que ya viene con Django
class FormUser(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "dni"
        ]