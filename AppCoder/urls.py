from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path("cursos/", views.cursos, name='Cursos'),
    path("cursosApi/", views.cursosapi),
    path("profesores/", views.profesores),
    path("busquedaCurso/", views.buscarcurso),
    path("buscar/", views.buscar),
    path("leerCurso/", views.leer_cursos),
    path("crearCurso/", views.crear_curso),
    path("editarCurso/", views.editar_curso),
    path("eliminarCurso/", views.eliminar_curso),
    path("cursos/list/", views.CursoList.as_view(), name='List'),
    path("cursos/create/", views.CursoCreate.as_view(), name='New'),
    path("cursos/edit/<pk>", views.CursoEdit.as_view(), name='Edit'),
    path("cursos/detail/<pk>", views.CursoDetail.as_view(), name='Detail'),
    path("cursos/delete/<pk>", views.CursoDelete.as_view(), name='Delete'),
]
