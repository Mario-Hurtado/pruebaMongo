from django.urls import path
from . import views
from .views import *
from django.conf.urls import url

urlpatterns = [

    url(r'^listaPedidos/', getPedidos)

]