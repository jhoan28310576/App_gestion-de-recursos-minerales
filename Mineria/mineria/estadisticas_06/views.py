from django.shortcuts import render
import plotly.express as px
from django.db.models import Count
from mineria_00.models import Mineral

# Create your views here.

def estadisticas(request):
    conteo_minerales = Mineral.objects.values('nombre').annotate(total=Count('nombre'))
    
    nombres = [item['nombre'] for item in conteo_minerales]
    totales = [item['total'] for item in conteo_minerales]
    
    fig = px.bar(x=nombres, y=totales, labels={'x':'Nombre del mineral', 'y':'Total'},title='Conteo de minerales')
    
    fig.write_html('static/grafico/mi_grafico.html')
    
    return render(request, 'estadisticas.html')
