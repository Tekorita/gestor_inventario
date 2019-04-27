from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from apps.usuario.forms import SignUpForm

#from .models import Perfil

#from .forms import SignUpForm

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'usuario/registrar.html'
    #succes_url = reverse_lazy('mascota_listar')
	
    def form_valid(self, form):
        '''
        En esta parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('login')
#succes_url = reverse_lazy('mascota_listar')
#class BienvenidaView(TemplateView):
#  template_name = 'perfiles/bienvenida.html'