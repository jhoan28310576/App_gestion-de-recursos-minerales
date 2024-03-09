from django.shortcuts import render
import plotly.express as px
from django.db.models import Count
from mineria_00.models import Mineral
from transporte_01.models import Transporte
from destino_02.models import Destino
from envio_03.models import Envio
from conductor_04.models import Conductor
from inspeccion_05.models import Inspeccion

# Create your views here.

def estadisticas(request):
    #-------------------------------------conteo_minerales---------------------
    conteo_minerales = Mineral.objects.values('nombre').annotate(total=Count('nombre'))
    
    nombres = [item['nombre'] for item in conteo_minerales]
    totales = [item['total'] for item in conteo_minerales]
    
    
    fig = px.bar(x=nombres, y=totales,color=nombres, labels={'x':'Nombre del mineral', 'y':'Total', 'color':'Nombres'},title='Conteo de minerales')
    fig.write_html('static/grafico/mi_grafico.html')
    
    #---------------------------------------Transportes-------------------------
    transportes = Transporte.objects.all()
    matriculas = [transportes.matricula for transportes in transportes ]
    tipos_transportes = [transportes.tipo_transporte for transportes in transportes]
    capacidades_carga =[float(transporte.capacidad_carga) for transporte in transportes] 

    if matriculas and capacidades_carga and tipos_transportes:
        fig2 = px.bar(x=matriculas, y=capacidades_carga, color=tipos_transportes, labels={'x':'Matricula', 'y':'Capacidad de carga', 'color':'tipos transportes'},title='Capacidad de carga por matriculas y tipo de transporte')
        fig2.write_html('static/grafico/mi_grafico_transporte.html')
    
    #---------------------------------------destino-------------------------
    destino = Destino.objects.all()
    estado = [destino.estado for destino in destino]
    ciudad = [destino.ciudad for destino in destino]
    
    if destino and estado and ciudad:
        fig3 = px.bar(x=estado, y=ciudad,color=ciudad, labels= {'x':'Estado', 'y':'ciudad', 'color':'Ciudad'}, title='Envios a los estados y ciudad')
        fig3.write_html('static/grafico/mi_grafico_destino.html')
    
    #---------------------------------------Envio-------------------------
    envio = Envio.objects.all()
    mineral = [str(envio.mineral) for envio in envio ]
    transporte = [str(envio.transporte) for envio in envio]
    destino = [str(envio.destino) for envio in envio]
    
    if mineral and transporte and destino:
        fig4 = px.bar(x=mineral, y=transporte, color=destino, labels={'x':'Mineral', 'y':'Transporte', 'color':'Destino'},title='Envio de minerales con el transporte al destino')
        fig4.write_html('static/grafico/mi_grafico_envio.html')
    
    #--------------------------------------Conductor--------------
    conductor = Conductor.objects.all()
    nombre = [conductor.nombre for conductor in conductor]
    licencia = [conductor.licencia for conductor in conductor]
    transporte  =[str(conductor.transporte) for conductor in conductor]
    
    if nombre and licencia and transporte:
        fig5 = px.bar(x=nombre, y=transporte, color=transporte, labels=
        {'x':'Nombre', 'y':'transporte', 'color':'Transporte'}, title='nombre conductor con la licencia y el transporte')
        fig5.write_html(('static/grafico/mi_grafico_conductor.html'))
    
    #--------------------------------------Inspeccion--------------
    inspeccion = Inspeccion.objects.all()
    envio = [str(inspeccion.envio) for inspeccion in inspeccion]
    fecha_inspeccion = [inspeccion.fecha_inspeccion for inspeccion in inspeccion]
    resultado  = [inspeccion.resultado for inspeccion in inspeccion]
    
    if inspeccion and envio and fecha_inspeccion and resultado: 
        fig6= px.bar(x=envio, y=fecha_inspeccion, color=resultado,  labels=
        {'x':'envio', 'y':'fecha_inspeccion', 'color':'Resultado'}, title='inspeccion de envio y resultado')
        fig6.write_html(('static/grafico/mi_grafico_Inspeccion.html'))
    
    return render(request, 'estadisticas.html')


