from .logic.logic_pedidos import getLatestXPedidos
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole, getUserEmail
from tendero.models import Tendero
from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId

#@login_required
@api_view(["GET", "POST"])
def getPedidos(request):
    role = getRole(request)

    email = getUserEmail(request)
 #   tendero = Tendero.objects.get(correo = email)

    if role == "Tendero Principal":
        client = MongoClient(settings.MONGO_CLI)
        db = client.canemdb
        pedidos1 = db['pedidos1']
        if request.method == "GET":
            result = []
            data = pedidos1.find({})
            for dto in data:
                jsonData = {
                    'id': str(dto['_id']),
                    "Nombre": str(dto['Nombre']),
                    'Precio': dto['Precio'],
                    "Categoría": str(dto['Categoría']),
                    "Descripción": str(dto['Descripción'])
            }
                result.append(jsonData)
            client.close()
            return JsonResponse(result, safe=False)
    
        if request.method == 'POST':
            data = JSONParser().parse(request)
            result = pedidos1.insert(data)
            respo ={
                "MongoObjectID": str(result),
                "Message": "nuevo objeto en la base de datos"
            }
            client.close()
            return JsonResponse(respo, safe=False)

    
        