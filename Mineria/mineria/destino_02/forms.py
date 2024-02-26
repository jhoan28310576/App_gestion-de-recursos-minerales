from django import forms
from .models import Destino

class Destinoform(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['estado', 'ciudad', 'direccion']