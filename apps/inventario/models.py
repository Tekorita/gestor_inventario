from django.db import models

# Create your models here.

class Inventario(models.Model):
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()