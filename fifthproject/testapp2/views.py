from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def show_response(request):
    s = "<h1>This is response from testapp2</h1>"
    return HttpResponse(s)
