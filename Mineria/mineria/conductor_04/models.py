from django.db import models
from transporte_01.models import Transporte

# Create your models here.

class Conductor(models.Model):#5
    nombre = models.CharField(max_length=200, blank=False)
    licencia = models.CharField(max_length=200, blank=False)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, blank=False)
    
    class Meta:
        db_table = 'Conductor'
        verbose_name = 'Conductor'
        verbose_name_plural = 'Conductores'
        
    def __str__(self):                 
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("Conductor", kwargs={"pk": self.pk})
    