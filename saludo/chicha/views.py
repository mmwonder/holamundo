from django.http import HttpResponse
from django.shortcuts import render

def hola(request):
    return HttpResponse("Hola mundo")

def chicha(request):
    return render(request,"inicio.html")