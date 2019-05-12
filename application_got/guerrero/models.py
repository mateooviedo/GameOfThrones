from django.db import models

# Create your models here.
class Guerrero(models.Model):
    nombre_guerrero = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    numero_muertes = models.IntegerField()
    isreinainteresada = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'guerrero'