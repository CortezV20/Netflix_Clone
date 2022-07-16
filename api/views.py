from http.client import ResponseNotReady
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Gary gil")

def inicio(request):
    return HttpResponse("Hola mundo")