from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('registrolibros/', views.registrar_libro, name='registrar_libro'),
    path('<int:el_id>/', views.detalle_libro, name='detalle_libro'),
    path('confirmacion/<int:libro_id>/', views.confirmacion_libro, name='confirmacion_libro'),
]