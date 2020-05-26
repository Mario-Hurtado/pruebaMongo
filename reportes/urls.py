from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_productos_mayor_rotacion, name='productoList')
]