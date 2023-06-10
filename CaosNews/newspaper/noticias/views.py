from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#def noticias(request):
#    return HttpResponse("Hello World")

def noticias(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())