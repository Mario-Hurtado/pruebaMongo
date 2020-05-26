from django.db import models
from ventas.models import Venta
from productoChiper.models import ProductoChiper

# Create your models here.
class ProductoVenta(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    producto = models.ForeignKey(ProductoChiper, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE , null = False , default=None)

    class Meta:
        db_table = 'PRODUCTOVENTA'
    
    def __str__(self):
        return '{}'.format(self.id)
