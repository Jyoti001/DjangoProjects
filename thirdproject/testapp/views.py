from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_response1(request):
    s = "<h1>This is Response 1</h1>"
    return HttpResponse(s)


def show_response2(request):
    s = "<h1>This is Response 2</h1>"
    return HttpResponse(s)

def show_response3(request):
    s = "<h1>This is Response 3</h1>"
    return HttpResponse(s)

def show_response4(request):
    s = "<h1>This is Response 4</h1>"
    return HttpResponse(s)
