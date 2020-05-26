from django.db import models
from productoChiper.models import ProductoChiper
from pedidos.models import Pedido


class ProductoPedido(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    producto = models.ForeignKey(ProductoChiper, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    subtotal = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE , default=None)

    class Meta:
        db_table = 'PRODUCTOPEDIDO'

    def __str__(self):
        return '{}'.format(self.producto.__getName__() + " : " + str(self.cantidad))
