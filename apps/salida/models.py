from django.db import models

# Create your models here.

class salida(models.Model): 
    nombre = models.CharField(max_length=100)
    categoria =models.CharField(max_length=100)
    cantidad = models.IntegerField()
    fecha_salida = models.TimeField(auto_now=True)

    def __str__(self):
        return self.nombre
