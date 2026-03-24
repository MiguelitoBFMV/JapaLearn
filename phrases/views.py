from django.shortcuts import render

def main_page(request):
    return render(request, "phrases/main_page.html")