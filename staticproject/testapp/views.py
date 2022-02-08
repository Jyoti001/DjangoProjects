from django.shortcuts import render

# Create your views here.

def WelcomeStatic(request):
    my_dict = {'msg1':'Orange','msg2':'Mango','msg3':'Banana'}
    return render(request,'testapp/ShowStatic.html',context=my_dict)
