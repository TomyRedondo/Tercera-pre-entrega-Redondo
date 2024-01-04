from django.urls import path
from .views import index, agregar_estudiante

urlpatterns = [
    path('', index, name='index'),
    path('agregar_estudiante/', agregar_estudiante, name='agregar_estudiante'),
    
    # Añadir URL necesarias
]