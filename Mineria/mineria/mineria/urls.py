"""
URL configuration for mineria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from gestion.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('gestion/', include('gestion.urls')),  
    path('mineria/', include('mineria_00.urls')), 
    path('transporte/', include('transporte_01.urls')), 
    path('destino/', include('destino_02.urls')), 
    path('envio/', include('envio_03.urls')), 
    path('conductor/', include('conductor_04.urls')), 
    path('inspeccion/', include('inspeccion_05.urls')), 
]
