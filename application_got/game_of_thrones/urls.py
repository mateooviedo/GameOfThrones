# Django
from django.urls import path
from django.shortcuts import render

# Views
from dragon import views as dragon_views
from guerrero import views as guerrero_views
from amante import views as amante_views
from territorio import views as territorio_views

def render_welcome_page(request):
    return render(request, 'welcome.html')

urlpatterns = [
    path('', render_welcome_page, name = "welcome"),
    path('dragones', dragon_views.admin_dragon, name = 'admin_dragon'),
    path('dragones/insert_dragon', dragon_views.insert_dragon, name = 'insert_dragon'),
    path('guerrero', guerrero_views.admin_guerrero, name = 'admin_guerrero'),
    path('guerrero/insert_guerrero', guerrero_views.insert_guerrero, name = 'insert_guerrero'),
    path('amante', amante_views.admin_amante, name = 'admin_amante'),
    path('amante/insert_amante', amante_views.insert_amante, name = 'insert_amante'),
    path('territorio', territorio_views.admin_territorio, name = 'admin_territorio'),
    path('territorio/insert_territorio', territorio_views.insert_territorio, name = 'insert_territorio'),
]
