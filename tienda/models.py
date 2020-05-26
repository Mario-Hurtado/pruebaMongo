from django.db import models
from zonas.models import Zona

# Create your models here.
class Tienda(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField( max_length=40 , default='Sin nombre')
    ingresos = models.BigIntegerField(null=False, blank=False)
    direccion = models.CharField(max_length=150, null=False, blank=False)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE , null = False , default=None)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    pais = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.direccion+"("+self.id+")")

    def getId(self):
        return self.id


