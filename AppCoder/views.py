from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
from django.core import serializers
from AppCoder.forms import CursoFormulario
from django.views.generic.detail import DetailView

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


def leer_cursos(request):
    cursos_all = Curso.objects.all()
    return HttpResponse(serializers.serialize('json', cursos_all))


def crear_curso(request):
    curso = Curso(nombre='CursoTest', camada=199, numero_dia=19)
    curso.save()
    return HttpResponse(f'Curso {curso.nombre} ha sido creado')


def editar_curso(request):
    nombre_consulta = 'CursoTest'
    Curso.objects.filter(nombre=nombre_consulta).update(
        nombre='NombreNuevoCursoTest')
    return HttpResponse(f'Curso {nombre_consulta} ha sido actualizado')


def eliminar_curso(request):
    nombre_nuevo = 'NombreNuevoCursoTest'
    curso = Curso.objects.get(nombre=nombre_nuevo)
    curso.delete()
    return HttpResponse(f'Curso {nombre_nuevo} ha sido eliminado')


class CursoList(ListView):
    model = Curso
    template = 'AppCoder/curso_list.html'


class CursoCreate(CreateView):
    model = Curso
    fields = '__all__'
    success_url = '/AppCoder/cursos/list/'


# Editar

class CursoEdit(UpdateView):
    model = Curso
    fields = '__all__'
    success_url = '/AppCoder/cursos/list/'


# Detalle
class CursoDetail(DetailView):
    model = Curso
    template = 'AppCoder/curso_detail.html'

# Borrar


class CursoDelete(DeleteView):
    model = Curso
    success_url = '/AppCoder/cursos/list/'
