from django.db import models

# Create your models here.
class Subdito(models.Model):
    nombre_subdito = models.CharField(max_length=30)
    aflicion = models.CharField(max_length=100)
    id_territorio = models.ForeignKey('Territorio', models.DO_NOTHING, db_column='id_territorio')

    class Meta:
        managed = False
        db_table = 'subdito'