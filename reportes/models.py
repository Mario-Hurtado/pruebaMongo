from django.db import models
from zonas.models import Zona
from productoChiper.models import ProductoChiper

class Reporte(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    fecha = models.DateTimeField()
    descripcion = models.CharField(max_length=80)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE , null = False , default=None)
    productos = models.ManyToManyField(ProductoChiper)
    
    def __str__(self):
        return '{}'.format(self.id + "-" + str(self.fecha))