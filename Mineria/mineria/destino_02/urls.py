from django.urls import path
from . import views
from .views import DeletedestinoView


urlpatterns = [
    path('', views.destino, name='destino'),
    path('listar', views.destino_list_view, name='destino_list_view'),
    path('load_destino_details/', views.load_destino_details, name='load_destino_details'), 
    path('delete_destino/<int:id>/', DeletedestinoView.as_view(), name='delete_destino'),
]


