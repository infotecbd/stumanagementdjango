from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    course = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
