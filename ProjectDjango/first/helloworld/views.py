from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def seasons(request):
    return HttpResponse('Зима, Весна, Лето, Осень')

def winter(request):
    return HttpResponse('Зима самый холодный сезон года')

def spring(request):
    return HttpResponse('Весной начинает все расцвитать ')

def summer(request):
    return HttpResponse('Лето самый жаркий сезон в году')

def autumn(request):
    return HttpResponse('Осень самый дождливый сезон в году')