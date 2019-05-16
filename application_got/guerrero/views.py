from django.shortcuts import render, redirect

# Models
from guerrero.models import Guerrero

# Create your views here.
def admin_guerrero(request):
  guerreros = Guerrero.get_all_guerreros()
  return render(request, 'guerrero/guerrero.html', { 'guerreros': guerreros })


def insert_guerrero(request):
  if request.method == 'POST':
    nombre_guerrero = request.POST['nombre_guerrero']
    especialidad = request.POST['especialidad']
    cargo = request.POST['cargo']
    numero_muertes = int(request.POST['numero_muertes'])
    isreinainteresada = bool(request.POST['isreinainteresada'])

    result = Guerrero.insert_Guerrero(nombre_guerrero, especialidad, cargo, numero_muertes, isreinainteresada)
    if result != None:
      return redirect('admin_guerrero')
  admin_guerrero(request)