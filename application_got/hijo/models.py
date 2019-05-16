from django.db import models

# Models
from subdito.models import Subdito

# Create your models here.
class Hijo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_hijo = models.CharField(max_length=30)
    id_subdito = models.ForeignKey(Subdito, models.DO_NOTHING, db_column='id_subdito')

    class Meta:
        managed = False
        db_table = 'hijo'

    
    def insert_Hijo(nombre_hijo, id_subdito):
        subdito = Subdito.objects.get(id = id_subdito)
        hijo = Hijo.objects.create(
            nombre_hijo = nombre_hijo,
            id_subdito = subdito
        )

        if hijo.pk:
            return hijo.pk
        return None
    

    def get_all_hijos():
        return Hijo.objects.all()