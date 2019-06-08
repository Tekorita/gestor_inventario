from django.db import models

# Create your models here.

class Personal(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self): #esta funcion nos trae el valor del objeto en vez del nombre del objeto cuando es llave foranea o forekeing
        return '{} {}'.format(self.nombre, self.apellido)

class Personal2(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)

    def __str__(self): #esta funcion nos trae el valor del objeto en vez del nombre del objeto cuando es llave foranea o forekeing
        return '{} {}'.format(self.nombre, self.apellido)