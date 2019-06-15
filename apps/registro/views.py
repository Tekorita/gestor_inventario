from django.shortcuts import render, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.registro.models import Registro
# Create your views here.

class RegistroList(ListView):
    model = Registro
    template_name = 'registro/listar.html'

class RegistroCreate(CreateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'registro/nuevo.html'
    success_url = reverse_lazy('registro_listar')

class RegistroUpdate(UpdateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'registro/nuevo.html'
    success_url = reverse_lazy('registro_listar')

class RegistroDelete(DeleteView):
    model = Personal
    template_name = 'personal/eliminar.html'
    success_url = reverse_lazy('personal_listar')

