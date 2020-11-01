from django.db import models
from django.utils import timezone


class Post(models.Model):#Definiendo un objeto.
#models.Model significa que Post es un modelo de Django,asi Django
#sabe que debe guardarlo en la base de datos.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)#este es una relacion(link) con otro modelo
    title = models.CharField(max_length=200)#texto con numero limitado de caracteres.
    text = models.TextField()#para textos largos sin limites.
    created_date = models.DateTimeField(
            default=timezone.now)#este es fecha y hora
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):#creando una funcion
        self.published_date = timezone.now()
        self.save()

    def __str__(self):#
        return self.title#devuelve 
