from django.db import models

# Create your models here.

class Mentor(models.Model):
    mentorid = models.CharField(max_length = 20, primary_key = True)
    mentorname = models.TextField(max_length = 50)
    nophone = models.TextField(max_length = 12)
    password = models.CharField(max_length = 10)

class Lecturer(models.Model):
    lecturerid = models.CharField(max_length = 20, primary_key = True)
    lecturername = models.TextField(max_length = 50)
    department = models.TextField(max_length = 30)
    password = models.CharField(max_length = 10)
    

class Student(models.Model):
    studentid = models.CharField(max_length = 20, primary_key = True)
    studentname = models.TextField(max_length = 50)
    nophone = models.TextField(max_length = 12)
    mentorid = models.ForeignKey(Mentor, on_delete = models.CASCADE)
    password = models.CharField(max_length = 10)

class Admin(models.Model):
    adminid = models.CharField(max_length = 20, primary_key = True)
    adminname = models.TextField(max_length = 150)
    position = models.TextField(max_length = 30)
    password = models.CharField(max_length = 10)

class Report(models.Model):
    lecturerid = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete = models.CASCADE)
    mentorid = models.ForeignKey(Mentor, on_delete = models.CASCADE)
    report = models.TextField(max_length = 150)
    date = models.DateField(null = True)
    status = models.TextField(max_length = 20, null=True)

