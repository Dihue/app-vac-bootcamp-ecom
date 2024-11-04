from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

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
    
    def clean_dni(self):
        dni = self.cleaned_data["dni"]

        if not ( 1 <= len(str(dni)) <= 8 ):
            raise ValidationError("DNI debe tener entre 7 y 8 dígitos")
        print(dni.__class__.__name__)

        return dni