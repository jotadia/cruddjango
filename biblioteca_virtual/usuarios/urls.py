from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('registro/', views.registrar_usuario, name='registrar_usuario'),
    path('<int:el_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('confirmacion/<int:usuario_id>/', views.confirmacion_usuario, name='confirmacion_usuario'),
]