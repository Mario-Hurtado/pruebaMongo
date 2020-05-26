from django.db import models

# Create your models here.
class Zona(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    nombre = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.id + "-" + self.nombre)