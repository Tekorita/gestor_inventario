from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.inventario.models import Inventario
# Create your views here.

class InventarioList(ListView):
    model = Inventario
    template_name = 'inventario/listar.html'

class InventarioCreate(CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/nuevo.html'
    success_url = reverze_lazy('inventario_listar')



