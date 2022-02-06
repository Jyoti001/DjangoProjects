from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_view1(request):
    return HttpResponse("<h1>Response from View1</h1>")

def show_view2(request):
    return HttpResponse("<h1>Response from View2</h1>")

def show_view3(request):
    return HttpResponse("<h1>Response from View3</h1>")
