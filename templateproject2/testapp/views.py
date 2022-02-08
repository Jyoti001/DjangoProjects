from django.shortcuts import render
import datetime
# Create your views here.

def show_cur_time(request):
    s = datetime.datetime.now()
    my_dict = {'dt':s}
    return render(request,'testapp/ShowTime.html',context=my_dict)
    #return render(request,'testapp/ShowTime.html',my_dict)
    #return render(request,'testapp/ShowTime.html',{'dt':s})    
