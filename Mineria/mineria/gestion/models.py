from django.db import models

# Create your models here.
      
class Mineral(models.Model):#1
    nombre = models.CharField(max_length=200)
    lugar_extraccion = models.CharField(max_length=200)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    pureza = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):                 
        return self.nombre

        
class Transporte(models.Model):#2 
    matricula = models.CharField(max_length=200)
    tipo_transporte = models.CharField(max_length=200)
    capacidad_carga = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_mantenimiento = models.DateField()
    
    def __str__(self):                 
        return self.matricula
      
class Destino(models.Model):#3
    estado = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    
    def __str__(self):                 
        return self.estado
     
class Envio(models.Model):#4
    mineral = models.ForeignKey(Mineral, on_delete=models.CASCADE)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    cantidad_mineral = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return str(self.mineral)

class Conductor(models.Model):#5
    nombre = models.CharField(max_length=200)
    licencia = models.CharField(max_length=200)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    
    def __str__(self):                 
        return self.nombre

class Inspeccion(models.Model):#6
    envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    fecha_inspeccion = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.envio)
