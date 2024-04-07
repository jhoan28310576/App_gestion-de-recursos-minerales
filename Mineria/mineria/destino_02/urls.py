from django.urls import path
from . import views

urlpatterns = [
    path('', views.destino, name='destino'),
    path('listar', views.destino_list_view, name='destino_list_view')
]


