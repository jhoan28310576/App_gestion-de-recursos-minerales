from django.urls import path
from . import views
from .views import DeletetransportView
urlpatterns = [
    path('', views.transporte, name='transporte'),
    path('listar/', views.transport_list_view, name='transport_list_view'), 
    path('load_transport_details/', views.load_transport_details, name='load_transport_details'),
    path('delete_transport/<int:id>/', DeletetransportView.as_view(), name='delete_transport'),
]
