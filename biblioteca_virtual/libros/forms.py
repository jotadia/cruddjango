from django import forms
from .models import Libro

class RegistroLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'fecha_publicacion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del libro'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Autor del libro'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del libro'
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            })
        }
