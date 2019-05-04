from django.urls import include, path
from apps.personal.views import PersonalList, PersonalCreate, PersonalUpdate

urlpatterns = [
    path('listar', PersonalList.as_view(), name='personal_listar'),
    path('nuevo', PersonalCreate.as_view(), name='personal_nuevo'),
    path('editar/<pk>/', PersonalUpdate.as_view(), name ='personal_editar'),
]