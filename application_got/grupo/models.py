from django.db import models

# Create your models here.
class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'grupo'


    def insert_grupo(nombre_grupo):
        grupo = Grupo.objects.create(
            nombre_grupo = nombre_grupo
        )
    
        if grupo.pk:
            return grupo.pk
        return None


    def get_all_grupos():
        return Grupo.objects.all()