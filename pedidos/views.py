from .logic.logic_pedidos import getLatestXPedidos
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole, getUserEmail
from tendero.models import Tendero

@login_required
def getPedidos(request):
    role = getRole(request)

    email = getUserEmail(request)
    tendero = Tendero.objects.get(correo = email)


    if role == "Tendero Principal":
        #query = request.GET.get('idTendero')
        #pedidos = getLatestXPedidos(str(query))
        pedidos = getLatestXPedidos(tendero.id)
        #pedidos_list = serializers.serialize('json',pedidos)
        return pedidos