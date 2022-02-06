from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def greet_user(request):
    dt = datetime.datetime.now()
    hour = int(dt.strftime('%H'))
    msg = "<h1>Hello Friend .... "
    if hour < 12:
        msg = msg + " Good Morning"
    elif hour < 16:
        msg = msg + " Good afternoon"
    elif hour < 21:
        msg = msg + "Good Evening"
    else:
        msg = msg + "Good Night"
    msg = msg + "</h1> <hr> Server time is " + str(dt)
    return HttpResponse(msg)
