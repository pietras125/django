from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a=4
    b=6
    c=a+b
    return HttpResponse("Hello, world. You're at the polls index. Wynik= ")