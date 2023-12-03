from django import forms
from . models import Usuario

class usuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'correo',
            'contraseña',
            'contraseña2',
            'telefono',
            'direccion',
        ]