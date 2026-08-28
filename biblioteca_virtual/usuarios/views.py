from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import RegistroUsuarioForm
from django.contrib import messages

import random


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, 'Usuario registrado exitosamente!')
            return redirect('confirmacion_usuario', usuario_id=usuario.id)
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})

def confirmacion_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'usuarios/confirmacion.html', {'usuario': usuario})

def inicio(request):
    mensaje = "¡Bienvenido a la Biblioteca Virtual!"
    r = random.randint(1,999)
    return render(request, 'usuarios/home.html',{"mensaje":mensaje,"r":r})

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listota.html',{"usuarios":usuarios})

def detalle_usuario(request, el_id):

    test = Usuario.objects.filter(id=el_id).exists()

    if test:
        el_usuario = Usuario.objects.get(id=el_id)
        return render(request, 'usuarios/detalle.html',{"usuario":el_usuario})
    else:
        return render(request,'usuarios/error_detalle.html')