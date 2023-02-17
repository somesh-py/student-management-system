from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('sign_in/',views.sign_in),
    path('courses/',views.courses),
    path('dashboard/',views.dashboard),
    path('employees/',views.employees),
    path('notifications/',views.notifications),
    path('pg_dashboard/',views.pg_dashboard),
    path('profile/',views.profile),
    path('sign-up/',views.sign_up),
    path('signup_data/',views.signup_updata),
    path('tables/',views.tables),
    path('tenants/',views.tenants),
    path('viewstudents/',views.viewstudents),
]
