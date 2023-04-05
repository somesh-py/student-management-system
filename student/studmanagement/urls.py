from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import apiviews

urlpatterns = [
    path('', views.index),
    path('sign_in/', views.sign_in),
    path('courses/', views.courses),
    path('addcourse/', views.addcourse),
    path('updateform/<int:uid>/', views.updatepage),
    path('updatecourse/', views.course_update),
    # path('delete/<int:uid>/',views.delete),
    re_path(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name="delete"),
    # path('updatecourse/<int:uid>/',views.courseupdate),
    # path('updatecoursedata/',views.course_update),
    path('dashboard/', views.dashboard),
    path('employees/', views.employees),
    path('notifications/', views.notifications),
    path('pg_dashboard/', views.pg_dashboard),
    path('profile/', views.profile),
    path('sign-up/', views.sign_up),
    path('signup_data/', views.signup_updata),
    path('tables/', views.tables),
    # students related start
    path('viewstudents/', views.viewstudents),
    path('sanjeev/<int:uid>', views.studentformid),
    path('studentupdatedata/', views.studentupdate),
    path('deletestudent/<int:uid>', views.deletestudent),
    path('addstudent/', views.addstudent),
    # student related end
    path('teachers/', views.teachers),
    path('addteacher/', views.tecaherdata),
    path('teacherupdate/<int:uid>/', views.teacherupdate),
    path('teacherupdatedata/', views.teacherupdatedata),
    path('deleteteacherdata/<int:uid>', views.deleteteacherdata),
    # 155514519
    # 0205

    # AddCourse api urls--->
    path('course/api/',apiviews.AddCourseGetandCreateApi.as_view()),
    path('course/api/<int:pk>',apiviews.AddCourseGetOnenadUpdateandDelete.as_view()),

    # AddStudent api urls--->
    path('student/api/',apiviews.AddStudentGetAllandCreateApi.as_view()),
    path('student/api/<int:pk>',apiviews.AddStudentGetOneandUpdateandDelete.as_view()),

    # AddTeacher api urls--->
    path('teacher/api/',apiviews.AddTeacherGetAllandCreateApi.as_view()),
    path('teacher/api/<int:pk>',apiviews.AddTeacherGetOneandUpdateandDeleteApi.as_view()),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
