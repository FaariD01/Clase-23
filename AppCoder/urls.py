from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path("cursos/", views.cursos, name='Cursos'),
    path("cursosApi/", views.cursosapi),
    path("profesores/", views.profesores),
    path("busquedaCurso/", views.buscarcurso),
    path("buscar/", views.buscar)


]
