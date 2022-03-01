from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course, Contact
from StudyCenter.models import StudyCenter, Book
from math import ceil

# Create your views here.
def index(request):
    # courses = Course.objects.all()
    # n = len(courses)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allCourses = []
    courseCategory = Course.objects.values('category', 'id')
    categoryC = {item['category'] for item in courseCategory}
    for cate in categoryC:
        course = Course.objects.filter(category=cate)
        n = len(course)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allCourses.append([course, range(1, nSlides), nSlides]) 

    # params = {'no_of_slides':nSlides, 'range':range(1,nSlides), 'course': courses}
    # allCourses = [[courses, range(1, nSlides), nSlides],
    #               [courses, range(1, nSlides), nSlides]]

    params = {'allCourses': allCourses}
    return render(request, 'course/index.html', params)

def about(request):
    return render(request, 'course/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(contact_name=name, contact_email=email, contact_phone=phone, contact_desc=desc)
        contact.save()
        messages.success(request, "Your message has been added successfully!")
    return render(request, 'course/contact.html')

def search(request):
    return render(request, 'course/search.html')

def courseView(request, myid):
    # Fetch the courses using id
    course = Course.objects.filter(id=myid)      
    return render(request, 'course/courseView.html', {'courses':course[0]})

def courseDetails(request, myid):
    course = Course.objects.filter(id=myid)   
    dcsa1201 = Book.objects.filter(book_title = 'DCSA 1201 - Computer Basics')
    dcsa1302 = Book.objects.filter(book_title = 'DCSA 1302 - Office Automation and MS Office')
    dcsa1303 = Book.objects.filter(book_title = 'DCSA 1303 - Computer Programming (NEW)')
    dcsa1304 = Book.objects.filter(book_title = 'DCSA 1304 - Visual Programming')
    dcsa2301 = Book.objects.filter(book_title = 'DCSA 2301 - Digital Systems & Computer Organization')
    dcsa2302 = Book.objects.filter(book_title = 'DCSA 2302 - Operating Systems')
    dcsa2303 = Book.objects.filter(book_title = 'DCSA 2303 - Internet Technology and Web Designing')
    courses = {
        "courses": course[0],
        "dcsa1201": dcsa1201,
        "dcsa1302": dcsa1302,
        "dcsa1303": dcsa1303,
        "dcsa1304": dcsa1304,
        "dcsa2301": dcsa2301,
        "dcsa2302": dcsa2302,
        "dcsa2303": dcsa2303
    }
    return render(request, 'course/courseDetails.html', courses)

def add_courseContent(request, myid):
    course = Course.objects.filter(id=myid)      
    # return render(request, 'course/courseView.html', {'courses':course[0]})
    return render(request, 'course/add_courseContent.html', {'courses':course[0]})

def checkout(request):
    return render(request, 'course/about.html')

def handleLogout(request):
    logout(request) 
    messages.success(request, "Successfully Logged Out")
    return redirect('CourseHome')  

def fix(request):
    course = Course.objects.all()
    # center = {
    #             "course_center": course
    #          }
    studyc = StudyCenter.objects.all()
    centerstudy = {
        "study_center": studyc,
        "course_center": course
    }
    return render(request, 'course/fix.html', centerstudy)
