from ..models import Reporte
from tienda.models import Tienda
from tendero.models import Tendero
from zonas.models import Zona
from reportes.models import Reporte
from productoChiper.models import ProductoChiper
import random

def get_productos_recomendados(id_tienda):
    zona_tienda = Tienda.objects.get(id=id_tienda)
    print(zona_tienda.nombre)
    zona_actual = zona_tienda.zona
    reporte_actual = Reporte.objects.filter(zona = zona_actual).order_by('-fecha')[:1]
    productos_recomendados = ProductoChiper.objects.filter(id__in = reporte_actual.values('productos'))

    return productos_recomendados