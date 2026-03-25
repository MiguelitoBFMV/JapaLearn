from django.contrib import admin
from django.urls import path

from phrases.views import main_page, consulta_datos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", main_page, name="Main Page"),
    path('consulta/', consulta_datos, name="Consulta de datos")
]
