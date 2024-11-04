from django.db import models

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    imagen = models.ImageField(upload_to='imagenes_perfil/', blank=True, null=True)

    def __str__(self):
        return self.nombre