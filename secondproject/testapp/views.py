from django.shortcuts import render
import datetime

# Create your views here.

from django.http import HttpResponse

def show_current_time(request):
    temp = datetime.datetime.now()
    s = "Current Time on Django Server is " + str(temp)
    return HttpResponse(s)
