from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_response(request):
    s = "<h1>This is response from testapp1</h1>"
    return HttpResponse(s)
