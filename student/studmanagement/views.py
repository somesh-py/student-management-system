from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http.response import HttpResponse
from django.contrib import messages
# Create your views here.

# index department start

def index(request):
    return render(request, 'index.html')


def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        ppassword = request.POST['password']
        if Student.objects.filter(email=email).exists():
            obj = Student.objects.get(email=email)
            mpassword = obj.password
            if check_password(ppassword, mpassword):
                return redirect('/courses/')
            else:
                return render(request, 'index.html', {'msg': 'password was incorrect'})
        else:
            return render(request, 'index.html', {'msg': 'email not exist'})

# index department end


# registration department start

def sign_up(request):
    return render(request, 'sign-up.html')


def signup_updata(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if Student.objects.filter(email=email).exists():
            messages.error(request, 'email already exist')
            return redirect('/sign-up/')
        else:
            Student.objects.create(name=name, email=email, password=password)
            messages.success(request, 'registration done sucessfully')
            return redirect('/sign-up/')


# registration department end



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



def tables(request):
    return render(request, 'tables.html')

# cousre department start

def courses(request):
    data = Addcourse.objects.all()
    return render(request, 'courses.html', {'data': data})


def addcourse(request):
    if request.method == 'POST':
        course = request.POST['course']
        fees = request.POST['fees']
        date = request.POST['date']
        comment = request.POST['comment']
        Addcourse.objects.create(
            course=course, fees=fees, date=date, comment=comment)
        data = Addcourse.objects.all()
        return render(request, 'courses.html', {'data': data})


def updatepage(request, uid):
    res = Addcourse.objects.get(id=uid)
    return render(request, 'updateform.html', {'i': res})


def course_update(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        ccourse = request.POST['ucourse']
        cfees = request.POST['ufees']
        ccomment = request.POST['ucomment']
        cdate = request.POST['uregistration']
        Addcourse.objects.filter(id=uid).update(
            course=ccourse, fees=cfees, comment=ccomment, date=cdate)
        return redirect('/courses/')


def delete(request, pk):
    res = Addcourse.objects.filter(id=pk).delete()
    return redirect('/courses/')

# course department end


# viewstudent start


def viewstudents(request):
    data = Addcourse.objects.all()
    studentdata = Addstudent.objects.all()
    return render(request, 'viewstudents.html', {'data': data, 'studentdata': studentdata})
    # return render(request, 'viewstudents.html')


def addstudent(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        college = request.POST.get('college')
        degree = request.POST.get('degree')
        stu_addcourse_id = request.POST.get('course')
        total_amount = request.POST.get('totalamount')
        paid_amount = request.POST.get('paidamount')
        due_amount = request.POST.get('dueamount')
        stu_course = Addcourse.objects.get(id=stu_addcourse_id)
        if Addstudent.objects.filter(semail=email).exists():
            messages.error(request, 'email already exist')
            return redirect('/viewstudents/')
        elif Addstudent.objects.filter(smobile=mobile).exists():
            messages.error(request, 'contact number is already exist')
        else:
            Addstudent.objects.create(sname=name, semail=email, smobile=mobile, saddress=address, scollege=college,
                                      sdegree=degree, scourse=stu_course, total_amount=total_amount, paid_amount=paid_amount, due_amount=due_amount)
        return redirect('/viewstudents/')


def studentformid(request, uid):
    uid = Addstudent.objects.get(id=uid)
    data = Addcourse.objects.all()
    return render(request, 'studentupdate.html', {'uid': uid, 'data': data})


def studentupdate(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        name = request.POST.get('sname')
        email = request.POST.get('semail')
        mobile = request.POST.get('smobile')
        address = request.POST.get('saddress')
        college = request.POST.get('scollege')
        degree = request.POST.get('sdegree')
        s_course = request.POST.get('course')
        stu_course = Addcourse.objects.get(id=s_course)
        Addstudent.objects.filter(id=uid).update(sname=name, semail=email, smobile=mobile, saddress=address, scollege=college, sdegree=degree,
                                                 scourse=stu_course)
        return redirect('/viewstudents/')


def deletestudent(request, uid):
    uid = Addstudent.objects.get(id=uid).delete()
    return redirect('/viewstudents/')

# end student section

# login required

# teachers department start


def teachers(request):
    sdata = Addcourse.objects.all()
    tdata = Addteachers.objects.all()
    return render(request, 'teachers.html', {'sdata': sdata, 'tdata': tdata})


def tecaherdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        employeeid = request.POST.get('employeeid')
        joiningdate = request.POST.get('joiningdate')
        experiance = request.POST.get('experiance')
        t_course = request.POST.get('course')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        timage = request.POST.get('image')
        password = make_password(request.POST.get('password'))
        stu_course = Addcourse.objects.get(id=t_course)
        Addteachers.objects.create(tname=name, employee_id=employeeid, joining_date=joiningdate, experiance=experiance,
                                   temail=email, tcontact=contact, tpassword=password, tcourses=stu_course, tgender=gender, tupload_image=timage)
        return redirect('/teachers/')
    
def teacherupdate(request,uid):
    uid=Addteachers.objects.get(id=uid)
    sdata = Addcourse.objects.all()
    return render(request,'teacherupdate.html',{'sdata': sdata,'uid':uid})

def teacherupdatedata(request):
    if request.method=='POST':
        uid=request.POST.get('uid')
        name=request.POST.get('name')
        employeeid=request.POST.get('employeeid')
        joiningdate=request.POST.get('joiningdate')
        experiance=request.POST.get('experiance')
        s_course=request.POST.get('course')
        email=request.POST.get('email')
        contact=request.POST.get('contact')
        t_course=Addcourse.objects.get(id=s_course)
        Addteachers.objects.filter(id=uid).update(tname=name, employee_id=employeeid, 
                                                  joining_date=joiningdate, experiance=experiance,
                                   temail=email, tcontact=contact, tcourses=t_course)
        return redirect('/teachers/')

def deleteteacherdata(request,uid):
    del_teacher=Addteachers.objects.get(id=uid).delete()
    return redirect('/teachers/')    
# add teacher data end
