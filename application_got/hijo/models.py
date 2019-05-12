from django.db import models

# Models
from subdito.models import Subdito

# Create your models here.
class Hijo(models.Model):
    nombre_hijo = models.CharField(max_length=30)
    id_subdito = models.ForeignKey(Subdito, models.DO_NOTHING, db_column='id_subdito')

    class Meta:
        managed = False
        db_table = 'hijo'