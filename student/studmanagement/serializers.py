from rest_framework import serializers
from .models import *


class AddCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addcourse
        fields='__all__'

class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addstudent
        fields='__all__'
    
class AddTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Addteachers
        fields='__all__'