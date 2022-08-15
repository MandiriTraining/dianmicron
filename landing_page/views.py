from django.shortcuts import render
from django.htpp import HttpResponse

def index(request):
   #return HttpResponse("Belajar Django Slur")
   return render(request, 'landing_page.html')
# Create your views here.
