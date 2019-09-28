from django.contrib import admin
from testapp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','eadd','esal']

admin.site.register(Employee,EmployeeAdmin)
