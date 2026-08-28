from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro   
from .forms import RegistroLibroForm
from django.contrib import messages

def registrar_libro(request):
    if request.method == 'POST':
        form = RegistroLibroForm(request.POST)
        if form.is_valid():
            libro = form.save()
            messages.success(request, 'Libro registrado exitosamente!')
            return redirect('confirmacion_libro', libro_id=libro.id)
    else:
        form = RegistroLibroForm()
    return render(request, 'libros/registrar_libros.html', {'form': form})

def confirmacion_libro(request, libro_id):
    libro = Libro.objects.get(id=libro_id)
    return render(request, 'libros/confirmacion.html', {'libro': libro})

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listota.html',{"libros":libros})


def detalle_libro(request, el_id):

    test = Libro.objects.filter(id=el_id).exists()

    if test:
        el_libro = Libro.objects.get(id=el_id)
        return render(request, 'libros/detalle.html',{"libro":el_libro})
    else:
        return render(request,'libros/error_detalle.html')