# Django
from django.shortcuts import render, redirect

# Models
from dragon.models import Dragon

# Create your views here.
def admin_dragon(request):
  dragones = Dragon.get_all_dragons()
  return render(request, 'dragon/dragon.html', { 'dragones': dragones })


def insert_dragon(request):
  if request.method == 'POST':
    disponible = bool(request.POST['disponible'])
    edad = int(request.POST['edad'])
    fuerza = int(request.POST['fuerza'])
    color = request.POST['color']
    nombre = request.POST['nombre']
    numero_muertes = int(request.POST['numero_muertes'])
    comida_favorita = request.POST['comida_favorita']

    # Inser database
    result = Dragon.insert_dragon(disponible, edad, fuerza, color, nombre, numero_muertes, comida_favorita)
    if result != None:
      return redirect('admin_dragon')

  admin_dragon(request)