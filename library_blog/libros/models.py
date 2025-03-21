from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField()
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
