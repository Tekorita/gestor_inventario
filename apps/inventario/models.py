from django.db import models

# Create your models here.

class Inventario(models.Model):
    descripcion = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()

    def __str__(self): #esta funcion nos trae el valor del objeto en vez del nombre del objeto cuando es llave foranea o forekeing
        return '{}'.format(self.descripcion)