from django.shortcuts import render

def main_page(request):
    texto = ""

    if request.method=="POST":
        texto = request.POST.get("frase_esp", "")
    return render(request, "phrases/main_page.html", {"frase_esp": texto})
