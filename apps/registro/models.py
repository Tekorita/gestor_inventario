from django.db import models
from apps.inventario.models import Inventario
from apps.personal.models import Personal
# Create your models here.

class Registro(models.model):
    personal = models.ForeignKey(Personal, null=True, blank=True, on_delete = models.CASCADE)
    insumo = models.ManyToManyField(Inventario, blank=True)
    cantidad = models.IntegerField()
    fecha = models.DateField()

    




