from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.personal.models import Personal 
from django.urls import reverse_lazy, reverse
from apps.personal.forms import PersonalForm

# Create your views here.

class PersonalList(ListView):
    model = Personal
    template_name = 'personal/listar.html'

class PersonalCreate(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'pesonal/nuevo.html'
    success_url = reverse_lazy('personal_listar')

class PersonalUpdate(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'personal/nuevo.html'
    success_url = reverse_lazy('personal_listar')
    
    
