from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def show_movie(request):
    head = "MOVIE NEWS"
    msg1 = "Movie News 1"
    msg2 = "Movie News 2"
    msg3 = "Movie News 3"
    msg4 = "Movie News 4"
    msg5 = "Movie News 5"
    type = "movies"
    my_dict = {'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4,'msg5':msg5,'type':type}
    return render(request,'testapp/News.html',context=my_dict)

def show_sports(request):
    head = "SPORTS NEWS"
    msg1 = "Sports News 1"
    msg2 = "Sports News 2"
    msg3 = "Sports News 3"
    msg4 = "Sports News 4"
    msg5 = "Sports News 5"
    type = "sports"
    my_dict = {'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4,'msg5':msg5,'type':type}
    return render(request,'testapp/News.html',context=my_dict)

def show_politics(request):
    head = "POLITICS NEWS"
    msg1 = "Politics News 1"
    msg2 = "Politics News 2"
    msg3 = "Politics News 3"
    msg4 = "Politics News 4"
    msg5 = "Politics News 5"
    type = "politics"
    my_dict = {'head':head,'msg1':msg1,'msg2':msg2,'msg3':msg3,'msg4':msg4,'msg5':msg5,'type':type}
    return render(request,'testapp/News.html',context=my_dict)
