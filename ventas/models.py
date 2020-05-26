from django.db import models
from tienda.models import Tienda

class Venta(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    ganancia = models.IntegerField()
    fecha = models.DateTimeField()
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE , null = False , default=None)

    def __str__(self):
        return '{}'.format(self.id + "-" + str(self.fecha))