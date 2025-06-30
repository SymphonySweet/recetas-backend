from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("¡Hola desde Render y Django somos el grupo 2 RECETAS DE COCINA Y MAS!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # ← esta línea muestra algo en la raíz "/"
]
