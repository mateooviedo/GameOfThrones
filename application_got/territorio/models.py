from django.db import models
from django.db.models import Count

# Create your models here.
class Territorio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_territorio = models.CharField(max_length=30)
    isconquistado = models.BooleanField()
    caracteristicas = models.TextField()
    clima = models.CharField(max_length=30)
    principales_productos = models.TextField()

    class Meta:
        managed = False
        db_table = 'territorio'

    
    def insert_territorio(nombre_territorio, isconquistado, caracteristicas, clima, principales_productos):
        territorio = Territorio.objects.create(
            nombre_territorio = nombre_territorio,
            isconquistado = isconquistado,
            caracteristicas = caracteristicas,
            clima = clima,
            principales_productos = principales_productos
        )

        if territorio.pk:
            return territorio.pk
        return None

    
    def get_all_territorios():
        return Territorio.objects.all()