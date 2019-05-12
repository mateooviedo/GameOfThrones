from django.db import models

# Create your models here.
class Grupo(models.Model):
    nombre_grupo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'grupo'