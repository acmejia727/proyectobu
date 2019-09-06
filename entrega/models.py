from django.db import models

# Create your models here.
class Entrega(models.Model):
    estado = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=100)
    fecha_reg = models.DateTimeField(auto_now=True)
       
    
