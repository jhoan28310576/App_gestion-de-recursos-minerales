from django.urls import path
from . import views

urlpatterns = [
    path('', views.inspeccion, name='inspeccion'),
    path('listar/', views.inspeccion_lista_view, name='inspeccion_lista_view'),
    #path('load_inspeccion_details/', views.load_inspeccion_details, name='load_inspeccion_details'),
    
]