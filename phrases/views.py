from django.shortcuts import render
from .services import translate_text
from .models import Categoria, Frase

def main_page(request):
    frase_esp = ""
    frase_jp = ""
    categoria = Categoria.objects.all()
    notas = ""
    categoria_elegida = ""
    
    if request.method=="POST":
        accion = request.POST.get("action")

        if accion == "translate":
            frase_esp = request.POST.get("frase_esp", "")
            frase_jp = translate_text(frase_esp)
        elif accion == "clear":
            frase_esp = ""
            frase_jp = ""
        elif accion == "save":
            frase_esp = request.POST.get("frase_esp", "")
            frase_jp = request.POST.get("frase_jp", "")
            notas = request.POST.get("notas")
            categoria_elegida = request.POST.get("categoria_id")
            if frase_esp and frase_jp and categoria_elegida:
                categoria_elemento = Categoria.objects.get(id=categoria_elegida)

                Frase.objects.create(
                    texto_esp = frase_esp,
                    texto_jp = frase_jp,
                    categoria = categoria_elemento,
                    nota = notas
                )


    return render(request, "phrases/main_page.html",
        {"frase_jp": frase_jp,
        "frase_esp": frase_esp,
        "notas": notas,
        "categorias": categoria})


def consulta_datos(request):
    registros = Frase.objects.all()

    return render(request, "phrases/consulta_datos.html", {"registros": registros})