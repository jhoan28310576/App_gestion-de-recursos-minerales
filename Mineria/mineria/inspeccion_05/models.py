from django.db import models
from ckeditor.fields import RichTextField
from envio_03.models import Envio

# Create your models here.

class Inspeccion(models.Model):#6
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE, blank=False)
    fecha_inspeccion = models.DateTimeField(auto_now_add=True, blank=False)
    resultado = RichTextField( blank=False)
    
    class Meta:
        db_table = 'Inspeccion'
        verbose_name = 'Inspeccion'
        verbose_name_plural = 'Inspecciones'
    
    def __str__(self):
        return str(self.envio)
    
    def get_absolute_url(self):
        return reverse("Inspeccion", kwargs={"pk": self.pk})