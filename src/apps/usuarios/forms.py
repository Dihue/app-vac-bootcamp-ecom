from django import forms

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