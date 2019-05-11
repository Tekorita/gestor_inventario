from django.urls import path, include
from apps.registro.views import RegistroList, RegistroCreate, RegistroUpdate, RegistroDelete

urlpatterns = [
    path('listar', RegistroList.as_view(), name='registro_listar'),
    path('nuevo', RegistroCreate.as_view(), name='registro_nuevo'),
    path('editar/<pk>/', RegistroUpdate.as_view(), name='registro_editar'),
    path('eliminar/<pk>/', RegistroDelete.as_view(), name='registro_eliminar'),
]