from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from django.core import serializers
from AppCoder.forms import CursoFormulario

# Create your views here.


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def cursos(request):
    if request.method == "POST":

        # Aqui me llega la informacion del html
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(
                nombre=informacion["curso"], camada=informacion["camada"], numero_dia=informacion["numero_dia"])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})


def profesores(request):
    return HttpResponse('Vista de Profesores')


def cursosapi(request):
    cursos_todos = Curso.objects.all()
    return HttpResponse(serializers.serialize('json', cursos_todos))


def buscar(request):
    camada_views = request.GET['camada']
    cursos_todos = Curso.objects.filter(camada=camada_views)
    return render(request, 'AppCoder/resultadoCurso.html', {"camada": camada_views, "cursos": cursos_todos})


def buscarcurso(request):
    return render(request, 'AppCoder/busquedaCurso.html')
