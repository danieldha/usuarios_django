from django.urls import path

from .views import CrearUsuarioView, ActualizarUsuarioView, ListarUsuarioView

app_name = 'gestion_usuarios'

urlpatterns = [
    path('listar', ListarUsuarioView.as_view(), name='listar_usuario'),
    path('crear', CrearUsuarioView.as_view(), name='crear_usuario'),
    path('actualizar/<str:pk>', ActualizarUsuarioView.as_view(), name='actualizar_usuario'),
]
