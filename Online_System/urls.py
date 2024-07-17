from django.urls import path
from . import views

urlpatterns = [
    path('', views.Account_Type, name='Account_Type'),
    path('Login_Lecturer', views.Login_Lecturer, name='Login_Lecturer'),
    path('Login_student', views.Login_student, name='Login_student'),
    path('Students', views.Students, name='Students'),
    path('Lecturers', views.Lecturers, name='Lecturers'),
    path('report', views.report, name='report'),
]

