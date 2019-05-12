from django.db import models

# Models
from grupo.models import Grupo

# Create your models here.
class Amante(models.Model):
    id_grupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='id_grupo')
    nombre_amante = models.CharField(max_length=30)
    isdigno = models.BooleanField(blank=True, null=True)
    isejecutado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amante'