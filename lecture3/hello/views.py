from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def abhi(request):
    return HttpResponse("Hello Abhi")

def david(request):
    return HttpResponse("hello david")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })