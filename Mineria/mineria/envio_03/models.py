from django.db import models
from mineria_00.models import Mineral
from transporte_01.models import Transporte
from destino_02.models import Destino
# Create your models here.

class Envio(models.Model):#4
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    cantidad_mineral = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        db_table = 'Envio'
        verbose_name = 'Envio'
        verbose_name_plural = 'Envios'
        
    def __str__(self):
        return str(self.mineral)
    
    def get_absolute_url(self):
        return reverse("Envio", kwargs={"pk": self.pk})