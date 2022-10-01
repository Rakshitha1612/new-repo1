from django.contrib import admin
from myapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
     l=['id','name','rollno','marks','address']
admin.site.register(Student,StudentAdmin)