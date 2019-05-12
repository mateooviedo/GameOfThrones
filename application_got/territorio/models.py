from django.db import models

# Create your models here.
class Territorio(models.Model):
    nombre_territorio = models.CharField(max_length=30)
    isconquistado = models.BooleanField()
    caracteristicas = models.TextField()
    clima = models.CharField(max_length=30)
    principales_productos = models.TextField()

    class Meta:
        managed = False
        db_table = 'territorio'