from django.shortcuts import render
from .logic.logic_reportes import get_productos_recomendados
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole, getUserEmail
from tendero.models import Tendero

@login_required
def get_productos_mayor_rotacion(request):
    role = getRole(request)
    email = getUserEmail(request)
    tendero = Tendero.objects.get(correo=email)
    if role == "Tendero Principal":
        productos = get_productos_recomendados(tendero.tienda.id)
        productos_list = serializers.serialize('json', productos)
        return productos
