from django.shortcuts import render, redirect

# Models
from territorio.models import Territorio
from subdito.models import Subdito

# Create your views here.
def admin_territorio(request):
  territorios = Subdito.get_all_territorios()
  return render(request, 'territorio/territorio.html', { 'territorios': territorios })


def insert_territorio(request):
  if request.method == 'POST':
    nombre_territorio = request.POST['nombre_territorio']
    isconquistado = bool(request.POST['isconquistado'])
    caracteristicas = request.POST['caracteristicas']
    clima = request.POST['clima']
    principales_productos = request.POST['principales_productos']

    result = Territorio.insert_territorio(nombre_territorio, isconquistado, caracteristicas, clima, principales_productos)
    if result != None:
      return redirect('admin_territorio')
  admin_territorio(request)
