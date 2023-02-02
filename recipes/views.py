from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def sobre(request):
    return HttpResponse("Hello Django!")


def contato(request):
    return HttpResponse("contato")
