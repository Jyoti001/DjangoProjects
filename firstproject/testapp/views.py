from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    temp_str = "<h1> Hello !!! Welcome to the first project of Django"
    return HttpResponse(temp_str)
