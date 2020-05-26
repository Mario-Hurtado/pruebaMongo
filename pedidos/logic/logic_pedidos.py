from ..models import Pedido
from tienda.models import Tienda
from tendero.models import Tendero
from productoPedido.models import ProductoPedido
from pedidos.models import Pedido
from productoChiper.models import ProductoChiper
from itertools import chain
import random

#ASR 2. Consultar el historial de pedidos en orden cronologico(se consultan los x ultimos)
def getLatestXPedidos(idTendero):

    #idTendero="1111"

    #Se hace un join de la tienda y el tendero
    tendero = Tendero.objects.get(id=idTendero)
    tiendaTendero = tendero.tienda

    #Se obtienen los pedidos y sus ids (correspondientes al Query)
    pedidos = Pedido.objects.filter(tienda = tiendaTendero).order_by('-fecha')[:5]  #Se define la cantidad de pedidos que el usuario quiere ver 
    idPedidos = []
    for pedido in pedidos:
        idPedidos.append(pedido.id)

    #Se obtienen los productos-pedido y sus ids (correspondientes al Query)
    productosPedido = ProductoPedido.objects.filter(pedido_id__in = idPedidos)
    idProductos = []
    for producto in productosPedido:
        idProductos.append(producto.id)

    #Se obtienen los productos-chiper y se concatenan jutno a productos-pedido y a los pedidos
    productosChiper = ProductoChiper.objects.filter(id__in = idProductos)
    listJson = list(chain(pedidos,productosPedido,productosChiper))

    return pedidos