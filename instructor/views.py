from django.shortcuts import render
from django.contrib import messages
from .models import Instructor, Assign_Course
import csv, io 
from account.models import User 
# Create your views here.

def add_instructor(request):
    instructor = Instructor.objects.all()
    template = "add_instructor.html"

    context = {
        "instructor": instructor,  
    }

    if request.method == "GET": 
        return render(request, template, context)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Instructor.objects.update_or_create(
            instructor_id = column[0],
            name = column[1],
            study_center = column[2],
            default_pass = column[3],
        ) 

        user = User()
        user.username = column[0]
        user.first_name = column[1].capitalize()
        user.set_password(column[3])
        user.is_active = True
        user.is_instructor = True
        user.save() 

    messages.success(request, "Instructor has been added successfully!")
    return render(request, template, context)

def assign_course(request):
    assignCourse = Assign_Course.objects.all()
    template = "assign_course.html"

    context = {
        "assignCourse": assignCourse,  
    }

    if request.method == "GET": 
        return render(request, template, context)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Assign_Course.objects.update_or_create(
            study_center = column[0], 
            instructor_id = column[1],
            assign_course = column[2],
            term = column[3],
            year = column[4],
        ) 

    messages.success(request, "Courses has been assigned successfully!")
    return render(request, template, context)
