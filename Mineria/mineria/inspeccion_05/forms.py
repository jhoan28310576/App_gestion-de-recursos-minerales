from django import forms
from .models import Inspeccion

class InspeccionForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = ['envio', 'resultado']
        widgets = {
            'envio': forms.Select(attrs={'class': 'form-control'}),
            'resultado': forms.Textarea(attrs={'class': 'form-control wide'}),
        }



