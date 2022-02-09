# DjangoProjects
####### IMPORTANT HANDS ON COMMANDS ###########\
\
django-admin startproject projectname\
python manage.py startapp testapp\
python manage.py runserver\
python manage.py runserver 7777\
urls.py - from testapp import views as v1 [to differentiate between multiple views of different apps]\
from django.urls import path,include [ in project level url]\
path('testapp/',include('testapp.urls'))\
TEMPLATE_DIR=BASE_DIR / 'templates'\
DIR = [TEMPLATE_DIR]\
return render(request, 'testapp/show_time.html',context=mydict) # mydict={'msg':value}, {{ msg}} - jinja2 coding, template tags, till template folder, already in settings.py file, so testapp/show_time.html path
\
STATIC_DIR = BASE_DIR / 'static' \
STATICFILES_DIRS = [STATIC_DIR] \
in the html file \
{% load static %} \
<img src="{% static 'images/fruits.jpg'%}" alt=""> \

###############################################\
1) **firstproject** - simple sayHello project [views/urls/settings]\
2) **secondproject** - return current time as response [views/urls/settings]\
3) **thirdproject** - one app,multiple views&url [views/urls/settings]\
4) **fourthproject** - single view but dynamic response, greet user based on server time [views/urls/settings]\
5) **fifthproject** - multiple apps single project[views/urls/settings]\
6) **sixthproject** - multiple apps with separate app level urls  - code reusability\
7) **templateproject1** - Introduction to template file, template folder in main project folder\
8) **templateproject2** - Dynamic response from template , template tag, in file styling, different ways of writing render in views\
9) **templateproject3** -Dynamic response,in file styling, random content\
10) **staticproject** -Loading static files like images and css\
11) **newsportal** - {% if %} - collaborated\
