from django.db import models
from envio_03.models import Envio

# Create your models here.

class Inspeccion(models.Model):#6
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    fecha_inspeccion = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'Inspeccion'
        verbose_name = 'Inspeccion'
        verbose_name_plural = 'Inspecciones'
    
    def __str__(self):
        return str(self.envio)
    
    def get_absolute_url(self):
        return reverse("Inspeccion", kwargs={"pk": self.pk})