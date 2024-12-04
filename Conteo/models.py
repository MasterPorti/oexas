from django.db import models

#Create your models here
class Gema(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    lote = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre