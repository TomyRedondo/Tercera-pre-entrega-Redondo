from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm, CursoForm
from .models import Estudiante, Profesor, Curso

def index(request):
    return render(request, 'index.html')

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})
