from typing import Any
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
    # Para crear un campo nuevo y personalizado
    # Hasta aquí no se mapea por lo que no se guardará
    # atributo1 = forms.CharField()

    # Para poder redefinir el tipo de campo y sus propiedades
    # username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(
            attrs={'placeholder':'Ingrese un nombre de usuario'}
        )
    )

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


    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)

        add_class_form_control = [
            "username",
            "first_name",
            "last_name",
            "email",
            "dni",
            "password1",
            "password2"
            ]
        
        for attr_field in add_class_form_control:
            self.fields[attr_field].widget.attrs["class"] = "form-control"
        
        self.fields["first_name"].widget.attrs["placeholder"] = "Ingrese su nombre"
        self.fields["last_name"].widget.attrs["placeholder"] = "Ingrese su apellido"


    def clean_dni(self):
        dni = self.cleaned_data["dni"]

        if not ( 1 <= len(str(dni)) <= 8 ):
            raise ValidationError("DNI debe tener entre 7 y 8 dígitos")
        print(dni.__class__.__name__)

        return dni