from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.inventario.models import Inventario
# Create your views here.

class InventarioList(ListView):
    model = Inventario
    template_name = 'inventariosss/listar.html'




