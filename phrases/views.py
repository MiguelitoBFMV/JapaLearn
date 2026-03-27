from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .services import translate_text
from .models import Categoria, Frase
from django.db.models import Q

CATEGORIA = Categoria.objects.all()

def main_page(request):
    frase_esp = ""
    frase_jp = ""
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
        "categorias": CATEGORIA})


def consulta_datos(request):
    registros = Frase.objects.all()
    categoria_id = request.GET.get("filtro_categoria")
    orden = request.GET.get("orden_elegido", "DESC")
    frase_eliminada = ""
    accion = request.GET.get("action")

    # METHOD POST
    if request.method=="POST":
        accion = request.POST.get("action")
        if accion == "delete":
            frase_eliminada = request.POST.get("registro_id")
            Frase.objects.filter(id=frase_eliminada).delete()
            return redirect("consulta_datos")
        
    # METHOD GET   
    if categoria_id:
        registros = Frase.objects.filter(categoria=categoria_id)
        categoria_id = int(categoria_id)

    # Filtro de orden
    if orden == "ASC":
        registros = registros.order_by("fecha")
    elif orden == "DESC":
        registros = registros.order_by("-fecha")

    # Realizar Búsquedas
    valor_buscado = request.GET.get("busqueda", "")

    if valor_buscado:
        registros = registros.filter(Q(texto_esp__icontains=valor_buscado) | Q(texto_jp__icontains=valor_buscado) | Q(nota__icontains=valor_buscado))
    
    # Limpiar los filtros
    if accion == "reset":
        return redirect("consulta_datos")

    

    
    return render(request, "phrases/consulta_datos.html", {"registros": registros, "categorias": CATEGORIA, "categoria_id": categoria_id, "orden": orden, "valor_buscado": valor_buscado})



def editar_datos(request, registro_id):

    registro_seleccionado = get_object_or_404(Frase, id=registro_id)

    if request.method=="POST" and request.POST.get("action") == "save_changes":
        frase_esp_mod = request.POST.get("frase_esp_mod")
        frase_jp_mod = request.POST.get("frase_jp_mod")
        categoria_mod = request.POST.get("categoria_mod")
        notas_mod = request.POST.get("nota_mod")

        if frase_esp_mod != "" and frase_jp_mod != "" and categoria_mod != "":
            registro_seleccionado.texto_esp = frase_esp_mod
            registro_seleccionado.texto_jp = frase_jp_mod
            registro_seleccionado.categoria_id = int(categoria_mod)
            registro_seleccionado.nota = notas_mod
            registro_seleccionado.save()

            return redirect("consulta_datos")


    return render(request, "phrases/editar_datos.html", {"registro": registro_seleccionado, "categorias": CATEGORIA})