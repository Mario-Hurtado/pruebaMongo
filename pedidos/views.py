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
from pymongo import MongoClient

#@login_required
#@api_view(["GET", "POST"])
'''def getPedidos(request):
    role = getRole(request)

    email = getUserEmail(request)
 #   tendero = Tendero.objects.get(correo = email)

 #   if role == "Tendero Principal":
    client = MongoClient(settings.MONGO_CLI)
    db = client.canemdb
    base = db['canemdb']
    if request.method == "GET":
        result = []
        data = base.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                "nombre": str(dto['nombre']),
                'precio': dto['precio'],
                "categoria": str(dto['categoria']),
                "descripcion": str(dto['descripcion'])
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = base.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
    client.close()
    return JsonResponse(respo, safe=False)'''

    



post1 = {"_id": 0, "nombre": "Alpin", "precio": 1500, "categoria": "Lacteos", "descripcion": "Leche achocolatada"}
post2 = {"_id": 1, "nombre": "Cigarrilos Kent", "precio": 8200, "categoria": "Abarrotes", "descripcion": "Tabaco para fumar"}

#collection.insert_one(post2)
'''results = collection.find()
for result in results:
    print(result)'''

def getPedidos(request):
    cluster = MongoClient("mongodb://monitoringUser:ISIS2503@clustertaller-shard-00-00-xvwem.mongodb.net:27017,clustertaller-shard-00-01-xvwem.mongodb.net:27017,clustertaller-shard-00-02-xvwem.mongodb.net:27017/test?ssl=true&replicaSet=ClusterTaller-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = cluster["canemdb"]
    collection = db["sugerencias"]
    if request.method == "GET":
        result = []
        datos = collection.find({})
        for dato in datos:
            jsonData = {

                'id': str(dato['_id']),
                "nombre": str(dato['nombre']),
                'precio': dato['precio'],
                "categoria": str(dato['categoria']),
                "descripcion": str(dato['descripcion'])

            }
            result.append(jsonData)
        cluster.close()
        return JsonResponse(result, safe = False)
    if request.method == "POST":
        datos = JSONParser().parse(request)
        result = collection.insert(datos)
        respuesta = {
            "MongoObjectID": str(result)
            "Message": "Nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respuesta, safe = False)
