from django.urls import path
from . import views

urlpatterns = [
    path('', views.envio, name='envio'),
    path('listar/', views.envio_list_view, name='envio_list_view'),
    path('load_envio_details/', views.load_envio_details, name='load_envio_details'),
    
]
