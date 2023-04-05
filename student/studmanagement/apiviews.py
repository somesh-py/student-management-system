from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *


# AddCourse api view -->

class AddCourseGetandCreateApi(generics.ListCreateAPIView):
    queryset=Addcourse.objects.all()
    serializer_class=AddCourseSerializer

class AddCourseGetOnenadUpdateandDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Addcourse.objects.all()
    serializer_class=AddCourseSerializer


# AddStudent api view -->
class AddStudentGetAllandCreateApi(generics.ListCreateAPIView):
    queryset=Addstudent.objects.all()
    serializer_class=AddStudentSerializer


class AddStudentGetOneandUpdateandDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset=Addstudent.objects.all()
    serializer_class=AddStudentSerializer

# AddTeachers api view -->

class AddTeacherGetAllandCreateApi(generics.ListCreateAPIView):
    queryset=Addteachers.objects.all()
    serializer_class=AddTeacherSerializer

class AddTeacherGetOneandUpdateandDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Addteachers.objects.all()
    serializer_class=AddTeacherSerializer