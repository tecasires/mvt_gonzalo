from django.db import models


class Familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_01 = models.CharField(max_length=50)
    apellido_02 = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=25, blank=True, null=True)
    ahorros = models.FloatField(max_length=10)
    active = models.BooleanField(default=True)
