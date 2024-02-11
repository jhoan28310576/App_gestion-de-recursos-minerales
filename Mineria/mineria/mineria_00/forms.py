from django import forms
from .models import Mineral

class Mineralform(forms.ModelForm):
    class Meta:
        model = Mineral
        fields = ['nombre', 'lugar_extraccion', 'peso', 'pureza' ]