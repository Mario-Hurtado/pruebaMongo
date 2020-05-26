from django.urls import path
from . import views

urlpatterns = [

    path('list/', views.get_tenderos, name='tenderoList'),
    path('tienda/', views.tenderoUI),
    path('listaPedidos/', views.tenderoListaPedidos, name = "listaPedidos"),
    path('recomendados/', views.tenderoListaRecomendados , name = "recomendados")

]