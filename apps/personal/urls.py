from django.urls import include, path
from apps.personal.views import ListView, CreateView, UpdateView

urlpatterns = [
    path('listar', ListView.as_view(), name='personal_listar'),
    path('nuevo', CreateView.as_view(), name='personal_nuevo'),
    path('editar' UpdateView.as_view(), name = 'personal_editar'),
]