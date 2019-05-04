from django.urls import include, path
from apps.personal.views import ListView, CreateView

urlpatterns = [
    path('listar', ListView.as_view(), name='personal_listar'),
    path('nuevo', CreateView.as_view(), name='personal_nuevo'),
]