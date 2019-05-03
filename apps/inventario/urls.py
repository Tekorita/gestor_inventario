from django.urls import path, include
from apps.inventario.views import InventarioList

urlpatterns = [
    path('listar', InventarioList.as_view(), name='inventario_listar'),
]