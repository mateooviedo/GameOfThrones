from django.db import models
from django.db.models import Count

# Models
from territorio.models import Territorio

# Create your models here.
class Subdito(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_subdito = models.CharField(max_length=30)
    aflicion = models.CharField(max_length=100)
    id_territorio = models.ForeignKey(Territorio, models.DO_NOTHING, db_column='id_territorio')

    class Meta:
        managed = False
        db_table = 'subdito'

    
    def insert_subdito(nombre_subdito, aflicion, id_territorio):
        territorio = Territorio.objects.get(id = id_territorio)
        subdito = Subdito.objects.create(
            nombre_subdito = nombre_subdito,
            aflicion = aflicion,
            id_territorio = territorio
        )

        if subdito.pk:
            return subdito.pk
        return None

    
    def get_all_subditos():
        return Subdito.objects.all()

    
    def get_all_territorios():
        territorios_no_conquistado = Territorio.objects.filter(isconquistado = False)
        territorios_conquistado = Subdito.objects.values('id_territorio').annotate(total=Count('id_territorio')).values(
            'id_territorio__nombre_territorio',
            'id_territorio__isconquistado',
            'id_territorio__caracteristicas',
            'id_territorio__clima',
            'id_territorio__principales_productos',
            'total')
        
        territorios = {
            'territorios_conquistado': territorios_conquistado,
            'territorios_no_conquistado': territorios_no_conquistado
        }

        return territorios
