from django.db import models


def crear_sin_categoria():
    return Categoria.objects.get_or_create(titulo="Sin Categoría")[0]

class Categoria(models.Model):
    titulo = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.titulo

class Frase(models.Model):
    texto_esp = models.TextField()
    texto_jp = models.TextField()
    categoría = models.ForeignKey(Categoria, on_delete=models.SET(crear_sin_categoria), related_name="Frases")
    nota = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto_esp