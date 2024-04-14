from django.urls import path
from . import views

urlpatterns = [
    path('', views.conductor, name='conductor'),
    path('listar/', views.conductor_list_view, name='conductor_list_view'), #me quede por aqui
    path('load_conductor_details/', views.load_conductor_details, name='load_conductor_details'), #me quede por aqui
]
