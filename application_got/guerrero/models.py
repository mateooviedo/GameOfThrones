from django.db import models

# Create your models here.
class Guerrero(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_guerrero = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    numero_muertes = models.IntegerField()
    isreinainteresada = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'guerrero'

    
    def insert_Guerrero(nombre_guerrero, especialidad, cargo, numero_muertes, isreinainteresada):
        guerrero = Guerrero.objects.create(
            nombre_guerrero = nombre_guerrero,
            especialidad = especialidad,
            cargo = cargo,
            numero_muertes = numero_muertes,
            isreinainteresada = isreinainteresada
        )

        if guerrero.pk:
            return guerrero.pk
        return None

    
    def get_all_guerreros():
        return Guerrero.objects.all()
