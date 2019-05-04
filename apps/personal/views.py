from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.personal.models import Personal 
from django.urls import reverse_lazy, reverse

# Create your views here.

class PersonalList(ListView):
    model = Personal
    template_name = 'personal/listar.html'
    
