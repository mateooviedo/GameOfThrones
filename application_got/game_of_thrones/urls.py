# Django
from django.urls import path
from django.conf import settings
from django.shortcuts import render

def render_welcome_page(request):
    return render(request, 'welcome.html')

urlpatterns = [
    path('', render_welcome_page, name = "welcome"),
]
