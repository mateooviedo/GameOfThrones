from django.db import models

class Dragon(models.Model):
    isdisponible = models.BooleanField()
    edad = models.IntegerField()
    fuerza = models.IntegerField()
    color = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    numero_muertes = models.IntegerField()
    comida_favorita = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dragon'
