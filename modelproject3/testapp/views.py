from django.shortcuts import render
from . import models
# Create your views here.

def show_employee(request):
    emp_list = models.Employee.objects.all()
    my_dict = {'emp_list':emp_list}
    return render(request,'testapp/Employee.html',context=my_dict)
