from django.shortcuts import render
from .models import Transporte
# Create your views here
def transporte(request):
    transporte = Transporte.objects.all()
    return render(request,'transporte.html',{"transportes":transporte})