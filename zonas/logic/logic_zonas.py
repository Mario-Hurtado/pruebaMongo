from django.db.models import Sum
from ..models import Zona
from tienda.models import Tienda
from ventas.models import Venta
from productoVenta.models import ProductoVenta
from productoChiper.models import ProductoChiper
from reportes.models import Reporte
import datetime
import schedule
import time

#ASR 1. Consultar las sugerencias de productos que tengan mayor rotación en la zona
def obtenerProductosMayorRotacionPorZona(zona_entrada):
    fecha_actual = date.today()
    corte_pasado = fecha_actual - timedelta(days=7)
    zona_actual = Zona.objects.filter(nombre = zona_entrada)[:1]
    tiendas_de_la_zona = Tienda.objects.filter(zona = zona_actual)
    ventas_de_las_tiendas = Venta.objects.filter(tienda__in = tiendas_de_la_zona).filter(fecha__range=[corte_pasado, fecha_actual])
    productosVenta_de_las_ventas = ProductoVenta.objects.filter(venta__in = ventas_de_las_tiendas).annotate(subtotal_ganancias = Sum('subtotal')).order_by('-subtotal_ganancias')[:20]
    productos_recomendados = ProductoChiper.objects.filter(id__in = productosVenta_de_las_ventas.values('producto'))
    
    return productos_recomendados

def actualizarProductosRecomendados():
    zonas = Zona.objects.values_list('nombre',flat=True)
    zonas = list(zonas)
    contador = 20
    for zona_actual in zonas:
        contador += 1
        id_generado = str(contador)
        productos_recomendados_en_zona = obtenerProductosMayorRotacionPorZona(zona_actual)
        fecha_actual = datetime.date.today()
        zona_buscada = Zona.objects.filter(nombre = zona_actual)
        descripcion_actual = 'Este reporte corresponde a la zona ' + zona_actual + ' y se genera el dia ' + str(fecha_actual)
        nuevo_reporte = Reporte.objects.create(id = id_generado, fecha = fecha_actual, descripcion = descripcion_actual, zona = zona_buscada.first())
        
        for prod in productos_recomendados_en_zona:
            nuevo_reporte.productos.add(prod)

actualizarProductosRecomendados()
schedule.every().saturday.at("22:00").do(actualizarProductosRecomendados)

while True:
    schedule.run_pending()
    time.sleep(30)
