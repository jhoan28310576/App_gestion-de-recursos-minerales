from django import forms
from .models import Transporte

class Transporteform(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = ['matricula', 'tipo_transporte', 'capacidad_carga', 'fecha_mantenimiento' ]