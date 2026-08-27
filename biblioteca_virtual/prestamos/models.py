from django.db import models  # type: ignore[import-untyped]


class Prestamo(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    libro = models.ForeignKey('libros.Libro', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo}"