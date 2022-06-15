from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante
# Create your views here.

def curso(self):

    curso = Curso(nombre= "web", camada = "11111")
    curso.save()
    documento = f"El curso es : {curso.nombre}, la camada: {curso.nombre}"
    return HttpResponse(documento)

def estudiantes(self):
    estudiante2 = Estudiante(nombre= "jonatan", camada = "11111")
    estudiante2.save
    documento = f"El estudiante es : {estudiante2.nombre}"
    return HttpResponse(documento)