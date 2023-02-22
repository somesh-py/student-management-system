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

class Addstudent(models.Model):
    sname=models.CharField(max_length=100)
    semail=models.EmailField(max_length=254)
    smobile=models.CharField(max_length=100)
    saddress=models.CharField(max_length=100)
    scollege=models.CharField(max_length=100)
    sdegree=models.CharField(max_length=100)
    # scourse=models.CharField(max_length=100)
    total_amount=models.IntegerField()
    paid_amount=models.IntegerField()
    due_amount=models.IntegerField()
    scourse=models.ForeignKey(Addcourse, on_delete=models.CASCADE)
    