from django.contrib import admin
from . import models

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['ename','eaddr','esal']

admin.site.register(models.Employee,EmployeeAdmin)
