from django.db import models  # type: ignore[import-untyped]


class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    fecha_publicacion = models.DateField()
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo