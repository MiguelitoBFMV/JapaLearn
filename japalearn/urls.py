from django.contrib import admin
from django.urls import path

from phrases.views import main_page, consulta_datos

urlpatterns = [
    path("", main_page, name="main_page"),
    path('consulta/', consulta_datos, name="consulta_datos"),
    path('admin/', admin.site.urls)
]
