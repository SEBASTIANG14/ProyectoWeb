from django import forms
from . models import Producto


class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'categoria', 
            'precio', 
        ]