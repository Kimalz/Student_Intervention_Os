from django.shortcuts import render,redirect
from Online_System.models import Lecturer,Student,Report,Mentor
from django.contrib import messages

# Create your views here.
def Account_Type(request):
    return render(request, 'Account_Type.html')

def Login_student(request):
    if request.method=='POST':
        studentname=request.POST.get('name')
        studentid=request.POST.get('Id')
        if Student.objects.filter(studentid=studentid,studentname=studentname):
            return redirect('Students') 
        else:      
            return render(request,'Login_student.html',{'error':'Invalid name or id ! Please re-enter'})
    else:
        return render(request,'Login_student.html')

def Login_Lecturer(request):
    if request.method=='POST':
        lecturername=request.POST.get('lecturername')
        lecturerid=request.POST.get('lecturerid')
        if Lecturer.objects.filter(lecturerid=lecturerid,lecturername=lecturername).exists():
            return redirect('Lecturers') 
        else:
            return render(request,'Login_Lecturer.html',{'error':'Invalid name or id ! Please re-enter'})
    else:return render(request,'Login_Lecturer.html')

def Students(request):
    return render(request, 'Students.html')

def Lecturers(request):
    lecturers = Lecturer.objects.all()
    students = Student.objects.all()
    mentors = Mentor.objects.all()
    
    if request.method == 'POST':
        lecturer_id = request.POST['lecturerid']
        lecturer = Lecturer.objects.get(lecturer_id)
        
        student_id = request.POST['studentid']
        student = Student.objects.get(student_id)
        
        mentor_id = request.POST.get['mentorid']
        mentor = Mentor.objects.get(mentor_id)
        
        report = request.POST['report']
        date = request.POST['date']
        status = request.POST['status']

        # Creating a new Report object and saving it
        report = Report(lecturerid=lecturer, studentid=student, mentorid=mentor, report=report, date=date, status=status)
        report.save()
        
        context = {
            'message': 'New data has been saved'
        }
        return render(request, 'Lecturers.html', context)
    else:
        context = {
            'lecturers': lecturers,
            'students': students,
            'mentors': mentors,
        }
    
    return render(request, "Lecturers.html", context)

def report(request):
    return render(request, 'Report.html')  
