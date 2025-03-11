from django.contrib import admin
from .models import Student

#class StudentAdmin(admin.ModelAdmin):
#    list_display = ['name', 'email', 'phone', 'course', ] 


# Register your models here.
admin.site.register(Student)