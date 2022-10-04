from django.shortcuts import render,redirect
from SchoolManagement.models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from SchoolManagement.forms import StudentForm
from django.contrib import messages

def index(request):
    all_students = Student.objects.all()
    context = {'all_students' : all_students}
    return render(request,'SchoolManagement/index.html',context)


def view_student(request,pk):
    all_students  = Student.objects.get(id=pk)
    context = {'all_students' : all_students}
    return HttpResponseRedirect(reverse('index'),context)


def create_student(request):
    
    if request.method == 'POST':
        create_student_form = StudentForm(request.POST)
        if create_student_form.is_valid():
            create_student_form.save()
            return render(request,'SchoolManagement/create_student.html',{
                'success' : True,
            }) 
    else:
        create_student_form = StudentForm()
    context = {'create_student_form' : create_student_form}
    return render(request,'SchoolManagement/create_student.html',context)


def update_student(request,pk):
    if request.method == 'POST':
        update_student = Student.objects.get(id=pk)
        update_student_form = StudentForm(request.POST,instance=update_student)
        if update_student_form.is_valid():
            update_student_form.save()
            return render(request,'SchoolManagement/edit_student.html',{'success' : True})

    else:
        update_student = Student.objects.get(id=pk)
        update_student_form = StudentForm(instance=update_student)
    context = {'update_student_form' : update_student_form}
    return render(request,'SchoolManagement/edit_student.html',context)


def delete_student(request,pk):
    if request.method == 'POST':
        delete_student = Student.objects.get(id=pk)
        delete_student.delete()
        return HttpResponseRedirect(reverse('index'))