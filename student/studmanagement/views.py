from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from .models import Student
from django.http.response import HttpResponse
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')
def sign_in(request):
    if request.method=='POST':
        email=request.POST['email']
        ppassword=request.POST['password']
        if Student.objects.filter(email=email).exists():
            obj=Student.objects.get(email=email)
            mpassword=obj.password
            if check_password(ppassword,mpassword):
                return redirect('/courses/')
            else:
                return render(request,'index.html',{'msg':'password was incorrect'})
        else:
            return render(request,'index.html',{'msg':'email not exist'})


def courses(request):
    return render(request, 'courses.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def employees(request):
    return render(request, 'employees.html')


def notifications(request):
    return render(request, 'notifications.html')


def pg_dashboard(request):
    return render(request, 'pg_dashboard.html')


def profile(request):
    return render(request, 'profile.html')


def sign_up(request):
    return render(request, 'sign-up.html')
def signup_updata(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password= make_password(request.POST['password'])
        if Student.objects.filter(email=email).exists():
            messages.error(request,'email already exist')
            return redirect('/sign-up/')
        else:
            Student.objects.create(name=name,email=email,password=password)
            messages.success(request,'registration done sucessfully')
            return redirect('/sign-up/')
def tables(request):
    return render(request,'tables.html')


def tenants(request):
    return render(request, 'tenants.html')


def viewstudents(request):
    return render(request, 'viewstudents.html')
