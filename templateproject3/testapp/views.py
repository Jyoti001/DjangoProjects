from django.shortcuts import render
import datetime
import random

# Create your views here.
def evaluate_response(request):
    time = datetime.datetime.now()
    hour = int(time.strftime('%H'))
    if hour < 12:
        s = 'Good Morning'
    elif hour < 16:
        s  = "Good Afternoon"
    elif hour < 21:
        s = "Good Evening"
    else:
        s = "Good Night"
    msg = 'Hello Friends ' + s

    names_list = ['AAA','BBB','CCC','DDD','EEE','FFF']
    greeting_list = [
    'Message 1',
    'Message 2','Message 3','Message 4','Message 5','Message 6','Message 7','Message 8','Message 9','Message 10']

    greet_name = random.choice(names_list)
    greet_msg = random.choice(greeting_list)
    my_dict = {'time':time,'msg':msg,'G_name':greet_name,'G_msg':greet_msg}
    return render(request,'testapp/Response.html',context = my_dict)
