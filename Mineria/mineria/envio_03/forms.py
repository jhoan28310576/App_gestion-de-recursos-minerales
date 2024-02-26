from django import forms
from .models import Envio

class Envioform(forms.ModelForm):
    class Meta:
        model = Envio
        fields = ['mineral', 'transporte', 'destino', 'cantidad_mineral']