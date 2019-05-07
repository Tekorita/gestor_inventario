from django.shortcuts import render
from django.views.generic import ListView
from apps.registro.models import Registro
# Create your views here.

class RegistroList(ListView):
    model = Registro
    template_name = 'registro/listar.html'