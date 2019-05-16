from django.db import models

class Dragon(models.Model):
    id = models.AutoField(primary_key=True)
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

    def insert_dragon(isdisponible, edad, fuerza, color, nombre, numero_muertes, comida_favorita):
        dragon = Dragon.objects.create(
            isdisponible = isdisponible,
            edad = edad,
            fuerza = fuerza,
            color = color,
            nombre = nombre,
            numero_muertes = numero_muertes,
            comida_favorita = comida_favorita
        )
        
        if dragon.pk:
            return dragon.pk
        return None

    
    def get_all_dragons():
        return Dragon.objects.all()