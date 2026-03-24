from django.shortcuts import render
from .services import translate_text

def main_page(request):
    frase_esp = ""
    frase_jp = ""

    if request.method=="POST":
        accion = request.POST.get("action")

        if accion == "translate":
            frase_esp = request.POST.get("frase_esp", "")
            frase_jp = translate_text(frase_esp)
        elif accion == "clear":
            frase_esp = ""
            frase_jp = ""

    return render(request, "phrases/main_page.html", {"frase_jp": frase_jp, "frase_esp": frase_esp})