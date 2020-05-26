from django.shortcuts import render
from .logic.logic_zonas import getProductsHighVolume
from django.http import HttpResponse
from django.core import serializers

def getZonas(request):
    zonas = getProductsHighVolume()
    zonas_list = serializers.serialize('json',zonas)
    
    return HttpResponse(zonas_list, content_type='application/json')

