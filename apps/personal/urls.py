from django.urls import include, path
from apps.personal.views import ListView

urlpatterns = [
    path('listar', ListView.as_view(), name='personal_listar'),
]