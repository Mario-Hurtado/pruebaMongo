from django.db import models
from tienda.models import Tienda


class Tendero(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    id = models.CharField(max_length=150, null=False, blank=False, primary_key=True)
    correo = models.EmailField(max_length=200)
    edad = models.PositiveSmallIntegerField()
    celular = models.CharField(max_length=80, null=False, blank=False)
    RUT = models.BigIntegerField(null=False, blank=False)
    tienda = models.OneToOneField(Tienda, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{}'.format(self.nombre + "(" + self.id + ")")

