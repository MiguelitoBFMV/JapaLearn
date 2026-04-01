from django.contrib import admin
from phrases.models import Categoria, Frase

@admin.register(Frase)
class FraseAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto_esp', 'categoria', 'usuario', 'fecha')
    search_fields = ('texto_esp', 'texto_jp', 'nota', 'usuario__username')
    list_filter = ('categoria', 'usuario', 'fecha')
    ordering = ('-fecha',)
    list_per_page = 20
    date_hierarchy = "fecha"
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    search_fields = ('titulo',)