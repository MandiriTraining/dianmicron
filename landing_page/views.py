from django.shortcuts import render
from django.htpp import HttpResponse

def index(request):
    return HttpResponse("Belajar Django Slur")
# Create your views here.
