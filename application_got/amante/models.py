from django.db import models

# Models
from grupo.models import Grupo

# Create your models here.
class Amante(models.Model):
    id = models.AutoField(primary_key=True)
    id_grupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='id_grupo')
    nombre_amante = models.CharField(max_length=30)
    isdigno = models.BooleanField(blank=True, null=True)
    isejecutado = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amante'

    
    def insert_amante(id_grupo, nombre_amante, isdigno, isejecutado):
        grupo = Grupo.objects.get(id = id_grupo)
        amante = Amante.objects.create(
            id_grupo = grupo,
            nombre_amante = nombre_amante,
            isdigno = isdigno,
            isejecutado = isejecutado
        )

        if amante.pk:
            return amante.pk
        return None

    
    def get_all_amantes():
        return Amante.objects.all()
