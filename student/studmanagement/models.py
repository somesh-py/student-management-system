from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class Addcourse(models.Model):
    course=models.CharField(max_length=100)
    fees=models.CharField(max_length=20000000)
    date=models.DateTimeField(auto_now_add=True)
    comment=models.CharField(max_length=100000000)