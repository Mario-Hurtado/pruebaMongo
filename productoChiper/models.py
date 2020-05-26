from django.db import models


# Create your models here.
class ProductoChiper(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=25)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=25)

    class Meta:
        db_table = 'PRODUCTOCHIPER'

    def __str__(self):
        return '{}'.format(self.nombre+"("+self.id+")")

    def __getName__(self):
        return self.nombre

    def __getPrice__(self):
        return self.precio

