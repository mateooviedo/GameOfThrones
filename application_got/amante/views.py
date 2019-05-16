from django.shortcuts import render, redirect
import random

# Models
from amante.models import Amante
from grupo.models import Grupo

# Create your views here.
def admin_amante(request):
  amantes = Amante.get_all_amantes()
  grupos = Grupo.get_all_grupos()
  return render(request, 'amante/amante.html', { 'amantes': amantes, 'grupos': grupos })


def insert_amante(request):
  if request.method == 'POST':
    id_grupo = int(request.POST['id_grupo'])
    nombre_amante = request.POST['nombre_amante']
    isdigno = bool(request.POST['isdigno'])
    isejecutado = id_grupo == 2

    if isdigno:
      isdigno = test_digno() > 10

    result = Amante.insert_amante(id_grupo, nombre_amante, isdigno, isejecutado)
    if result != None:
      return redirect('admin_amante')

  admin_amante(request)


def test_digno():
  digno = "digno"
  nodigno = "no digno"
  prob = 0.9
  cant = 100
  lista = [nodigno]*int(prob*cant)+[digno]*int((1-prob)*cant)

  resultados = {digno: 0, nodigno: 0}
  for i in range(1000):
    resultados[random.choice(lista)] +=1

  prob_digno = (100*resultados[digno])/(resultados[digno] + resultados[nodigno])
  return prob_digno