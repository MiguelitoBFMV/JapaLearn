from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from phrases.views import main_page, consulta_datos, editar_datos

urlpatterns = [
    path("", main_page, name="main_page"),
    path('consulta/', consulta_datos, name="consulta_datos"),
    path('editar/<int:registro_id>/', editar_datos, name="editar_datos"),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="phrases/login.html"))
]
