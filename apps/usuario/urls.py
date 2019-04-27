from django.urls import path, include

from apps.usuario.views import SignUpView

urlpatterns = [
	#path('registrar', ver_datos, name='registrar'),
	path('registrar', SignUpView.as_view(), name='sign_up'),
]