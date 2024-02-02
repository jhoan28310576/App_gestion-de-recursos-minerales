from django.shortcuts import render

# Create your views here.
def destino(resquest):
    return render(resquest, 'destino.html')