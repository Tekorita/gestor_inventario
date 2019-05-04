from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.inventario.models import Inventario
from apps.inventario.forms import InventarioForm
# Create your views here.

class InventarioList(ListView):
    model = Inventario
    template_name = 'inventario/listar.html'

class InventarioCreate(CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/nuevo.html'
    success_url = reverse_lazy('inventario_listar')

class InventarioUpdate(UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/nuevo.html'
    success_url = reverse_lazy('inventario_listar')

class InventarioDelete(DeleteView):
    model = Inventario
    template_name = 'inventario/eliminar.html'
    success_url = reverse_lazy('inventario_listar')



