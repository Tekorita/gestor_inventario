from django.urls import path, include
from apps.inventario.views import InventarioList, InventarioCreate, InventarioUpdate, InventarioDelete

urlpatterns = [
    path('listar', InventarioList.as_view(), name='inventario_listar'),
    path('nuevo', InventarioCreate.as_view(), name='inventario_nuevo'),
    path('editar/<pk>/', InventarioUpdate.as_view(), name='inventario_editar'),
    path('eliminar/<pk>/', InventarioDelete.as_view(), name='inventario_eliminar'),
]