from django.urls import include, path
from gestion.admin import admin_site
from django.conf import  settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin_site.urls),
    path('gestion/', include('gestion.urls'), name='index'),  
    path('mineral_create_view/', include('mineria_00.urls'), name='mineral_create_view'), 
    path('transporte/', include('transporte_01.urls'), name='transporte'), 
    path('destino/', include('destino_02.urls'), name='destino'), 
    path('envio/', include('envio_03.urls'), name='envio'), 
    path('conductor/', include('conductor_04.urls'), name='conductor'), 
    path('inspeccion/', include('inspeccion_05.urls'), name='inspeccion'),
    path('img/', include('inspeccion_05.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
