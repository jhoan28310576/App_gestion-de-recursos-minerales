from django import forms
from .models import Conductor

class Conductorform(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = ['nombre', 'licencia', 'transporte']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'licencia': forms.TextInput(attrs={'class': 'form-control'}),
            'transporte': forms.Select(attrs={'class': 'form-control'}),
        }
