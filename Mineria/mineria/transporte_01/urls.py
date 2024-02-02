from django.urls import path
from . import views

urlpatterns = [
    path('', views.transporte, name='transporte'),
]
