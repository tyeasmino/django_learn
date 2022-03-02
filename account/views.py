from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from StudyCenter.forms import CenterCreateForm, CenterBookForm, CenterRoutineForm
from django.contrib.auth import authenticate, login, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.auth.forms import PasswordChangeForm
from account.models import User_Detail
from django.contrib import messages
from course.models import Course, Contact
from StudyCenter.models import StudyCenter, Book, Routine
from area.models import Country, Division, District, Area
from math import ceil
import json 
from django.core.files.storage import FileSystemStorage

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader  import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
UserModel = get_user_model()

# Create your views here.

def register(request):   
    course = Course.objects.all()
    if request.method == 'POST':
        con = request.POST["contact"]        
        if len(request.FILES) != 0:
            profile = request.FILES['u-img']
        usercourse = request.POST["usercourse"]
        print(usercourse)
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()   
            ucourse = Course.objects.get(pk=usercourse)
            details = User_Detail(user= user, contact_Number= con, user_Profile = profile, user_course = ucourse)     
            details.save() 

            current_site = get_current_site(request)
            mail_subject='Activate Your Account'
            message=render_to_string('email.html',{
                'user':user,
                'domain':  current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
        
            send_mail = form.cleaned_data.get('email')
            email=EmailMessage(mail_subject, message, to=[send_mail])
            email.send()
            
            messages.success(request, "Your account has been created successfully!")             
            messages.info(request, "Activate your account from the mail you provided")             
            return render(request,'register.html', {'form': form, "course": course})            
        else:
            msg = 'form is not valid'
            messages.info(request, "Your form is not valid!") 
    else: 
        form = SignUpForm()
    return render(request,'register.html', {'form': form, "course": course, 'msg': messages})

def activate(request, uidb64, token):
    try: 
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None 

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Your account is activated now, you can now log in") 
        return redirect('login_view')        
    else: 
        messages.warning(request, "Activation link is invalid")
        return redirect('register') 

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            elif user is not None and user.is_learner:
                login(request, user)
                return redirect('learner')
            elif user is not None and user.is_instructor:
                login(request, user)
                return redirect('instructor')
            else:
                messages.info(request, "Invalid Credentials!")                
        else:
            messages.error(request, "error validating form")
    return render(request, 'login.html', {'form': form, 'msg': messages})

@login_required
def change_password(request): 
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            messages.success(request, "Your password has changed successfully!")
            return redirect('CourseHome')
    else: 
        form=PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form':form})

@login_required
def admin(request):
    courseBOU = Course.objects.filter(subcategory = 'BOU')
    course = Course.objects.all()
    contact = Contact.objects.all()
    dcsa_routine = Routine.objects.filter(routine_of_the_course = 20)
    cse_routine = Routine.objects.filter(routine_of_the_course = 19)
    # center = {
    #             "course_center": course
    #          }
    studyc = StudyCenter.objects.all()
    centerstudy = {
        "study_center": studyc,
        "course_center": course, 
        "course_bou": courseBOU, 
        "contact": contact,
        "dcsa_routine": dcsa_routine,
        "cse_routine": cse_routine
    }
    return render(request,'admin.html', centerstudy)

@login_required
def learner(request):
    return render(request,'learner.html')

@login_required
def instructor(request):
    allCourses = []
    courseCategory = Course.objects.values('course_designed_by')
   
    course = Course.objects.filter(course_designed_by = request.user.username)
    n = len(course)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    allCourses.append([course, range(1, nSlides), nSlides]) 
    
    params = {'allCourses': allCourses}
    return render(request,'instructor.html', params)

@login_required
def learnerprofile(request):
    return render(request,'learnerprofile.html')

@login_required
def learnernotes(request):
    return render(request,'learner_notes.html')

@login_required
def pickcourse(request):
    country = Country.objects.all().order_by('name')
    country_list = list(country.values('name', 'id'))
    country_list = json.dumps(country_list)

    division = Division.objects.all().order_by('name')
    division_list = list(division.values('name', 'country__name', 'id'))
    division_list = json.dumps(division_list)

    district = District.objects.all().order_by('name')
    district_list = list(district.values('name','division__name', 'id'))
    district_list = json.dumps(district_list)

    context = {
        "country_list": country_list, 
        "division_list": division_list, 
        "district_list": district_list, 
    } 

    return render(request, 'pickcourse.html', context) 

@login_required
def instructorprofile(request):
    return render(request,'instructorprofile.html')

@login_required
def manageCourse(request):
    if request.method == "POST":
        # c_img = request.POST.get('c-img', '')
        c_name = request.POST.get('c-name', '')
        c_designed_by = request.POST.get('c-designed-by', '')
        c_category = request.POST.get('c-category', '')
        c_subcategory = request.POST.get('c-subcategory', '')
        c_desc = request.POST.get('c-desc', '')
        c_date = request.POST.get('c-date', '')
        c_price = request.POST.get('c-price', '')
        c_aim1 = request.POST.get('c-aim1', '')
        c_aim2 = request.POST.get('c-aim2', '')
        c_aim3 = request.POST.get('c-aim3', '')
        c_aim4 = request.POST.get('c-aim4', '')
        c_aim5 = request.POST.get('c-aim5', '')

        if len(request.FILES) != 0:
            c_img = request.FILES['c-img']

        course = Course(course_name=c_name, course_designed_by=c_designed_by, category=c_category, subcategory=c_subcategory, desc=c_desc, release_date=c_date, course_price=c_price, course_image=c_img, course_aim1=c_aim1, course_aim2=c_aim2, course_aim3=c_aim3, course_aim4=c_aim4, course_aim5=c_aim5)
        course.save() 
        messages.success(request, "Your course has been added successfully!")  
    return render(request,'manageCourse.html')

@login_required
def handleLogout(request):
    logout(request) 
    messages.success(request, "Successfully Logged Out")
    return redirect('CourseHome')  

@login_required
def myCourses(request):
    course = Course.objects.filter(course_designed_by = request.user.username)      
    course = {       
        "course_center": course
    }   
    return render(request, 'myCourses.html', course)


# Study Center Database Handles
# ------------------------------- 

# This function adds data in Study Center from admin and shows in table 
@login_required
def add_studyCenter(request):
    studyc = StudyCenter.objects.all()
    form = CenterCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your study Center has been added successfully!")
    context = {
        "form": form,      
        "study_center": studyc,  
    }
    return render(request, 'add_studyCenter.html', context)

# This function deletes data from Study Center database from admin
@login_required
def delete_studyCenter(request, id):
    if request.method == "POST":
        id = StudyCenter.objects.get(pk=id)
        id.delete()
        messages.success(request, "Your study center has been deleted successfully!")
        return redirect('add_studyCenter') 

@login_required
def update_studycenter(request, id):  
    if request.method == "POST":
        print(id)
        us = StudyCenter.objects.get(pk=id)
        form = CenterCreateForm(request.POST, instance=us)
        if form.is_valid():
            form.save() 
        messages.success(request, "Your study center has been updated successfully!")
    else:
        us = StudyCenter.objects.get(pk=id)
        form = CenterCreateForm(instance=us) 
    return render(request, 'update_studycenter.html', {'form':form}) 

# Book Database Handles 
# -----------------------

# This function adds data in Book database from admin and shows in table
@login_required
def add_books(request):
    books = Book.objects.all()
    form = CenterBookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your book has been added successfully!")
    context = {
        "form": form,   
        "books": books,     
    }
    return render(request, 'add_books.html', context)

# This function deletes data from Book database from admin
@login_required
def delete_book(request, id):
    if request.method == "POST":
        id = Book.objects.get(pk=id)
        id.delete()
        messages.success(request, "Your book has been deleted successfully!")
        return redirect('add_books') 

@login_required
def update_book(request, id):
    ub = Book.objects.get(pk=id) 
    if request.method == "POST":
        form = CenterBookForm(request.POST, instance=ub)
        if form.is_valid():
            form.save()
        messages.success(request, "Your book has been updated successfully!")
    else:
        ub = Book.objects.get(pk=id)
        form = CenterBookForm(instance=ub)
    return render(request, 'update_books.html', {'form':form, 'id':id}) 

@login_required
def update_bookFile(request, id):
    if request.method == "POST":      
        book_file = request.FILES['book_file']
        file_name = request.FILES['book_file'].name

        fs = FileSystemStorage()
        file = fs.save(book_file.name, book_file)
        fileurl = fs.url(file)
        report = file_name

        Book.objects.filter(pk = id).update(book_file = book_file)
        messages.success(request, "Your book file has been updated successfully!")
        ur = Book.objects.get(pk=id)
        form = CenterBookForm(instance=ur) 
        return redirect(add_books)
    else: 
        return render(request, 'update_books.html', {'form':form, 'id':id})   


# Routine Database Handles
# ------------------------- 

# This function adds data in Routines database from admin and shows in table 
@login_required
def add_routines(request):
    routine = Routine.objects.all()
    form = CenterRoutineForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Your routine has been added successfully!")
    context = {
        "form": form,   
        "routine": routine,     
    }
    return render(request, 'add_routines.html', context)

# This function deletes data from Routine database from admin
@login_required
def delete_routine(request, id):
    if request.method == "POST":
        id = Routine.objects.get(pk=id)
        id.delete()
        messages.success(request, "Your routine has been deleted successfully!")
        return redirect('add_routines')

@login_required
def update_routine(request, id): 
    ur = Routine.objects.get(pk=id) 
    if request.method == "POST":      
        form = CenterRoutineForm(request.POST, instance=ur) 
        if form.is_valid():
            form.save()
        messages.success(request, "Your routine has been updated successfully!")
    else:
        ur = Routine.objects.get(pk=id)
        form = CenterRoutineForm(instance=ur)
    return render(request, 'update_routines.html', {'form':form, 'id':id}) 

@login_required
def update_routineFile(request, id):  
    if request.method == "POST":      
        routine_file = request.FILES['routine_file']
        file_name = request.FILES['routine_file'].name

        fs = FileSystemStorage()
        file = fs.save(routine_file.name, routine_file)
        fileurl = fs.url(file)
        report = file_name

        Routine.objects.filter(pk = id).update(routine_file = routine_file)
        messages.success(request, "Your routine file has been updated successfully!")
        ur = Routine.objects.get(pk=id)
        form = CenterRoutineForm(instance=ur) 
        return redirect(add_routines)
    else: 
        return render(request, 'update_routines.html', {'form':form, 'id':id})   
   
# Course Database Handles
# ------------------------- 

# This function adds data in Course database from admin and shows in table 
@login_required
def add_course(request):
    if request.method == "POST":
        c_name = request.POST.get('c-name', '')
        c_designed_by = request.POST.get('c-designed-by', '')
        c_category = request.POST.get('c-category', '')
        c_subcategory = request.POST.get('c-subcategory', '')
        c_desc = request.POST.get('c-desc', '')
        c_date = request.POST.get('c-date', '')
        c_price = request.POST.get('c-price', '')
        c_aim1 = request.POST.get('c-aim1', '')
        c_aim2 = request.POST.get('c-aim2', '')
        c_aim3 = request.POST.get('c-aim3', '')
        c_aim4 = request.POST.get('c-aim4', '')
        c_aim5 = request.POST.get('c-aim5', '')

        if len(request.FILES) != 0:
            c_img = request.FILES['c-img']

        course = Course(course_name=c_name, course_designed_by=c_designed_by, category=c_category, subcategory=c_subcategory, desc=c_desc, release_date=c_date, course_price=c_price, course_image=c_img, course_aim1=c_aim1, course_aim2=c_aim2, course_aim3=c_aim3, course_aim4=c_aim4, course_aim5=c_aim5)
        course.save() 
        messages.success(request, "Your course has been added successfully!")  
    course = Course.objects.all()
    return render(request,'add_course.html', {"course": course,})

# This function deletes data from Course database from admin
@login_required
def delete_course(request, id):
    if request.method == "POST":
        id = Course.objects.get(pk=id)
        id.delete()
        messages.success(request, "Your course has been deleted successfully!")
        return redirect('add_course') 

# Not Done
@login_required
def update_course(request, id):
    course = Course.objects.get(pk=id)

    if request.method == "POST":
        # if len(request.FILES) != 0:
        #     if len(course_image) > 0:
        #         os.remove(course_image.path)
        #     c_img = request.FILES['c-img'] 
        
        course.course_name = request.POST['c_name']
        course.course_designed_by = request.POST['c_designed_by']
        course.category = request.POST['c_category']
        course.subcategory = request.POST['c_subcategory']
        course.desc = request.POST['c_desc']
        course.course_price = request.POST['c_price']
        course.course_aim1 = request.POST['c_aim1']
        course.course_aim2 = request.POST['c_aim2']
        course.course_aim3 = request.POST['c_aim3']
        course.course_aim4 = request.POST['c_aim4']
        course.course_aim5 = request.POST['c_aim5'] 

        course.save() 
        messages.success(request, "Your course has been updated successfully!")  
    
    return render(request, 'update_course.html', {"course": course, "id": id}) 

@login_required
def update_courseFile(request, id):
    if request.method == "POST":      
        course_image = request.FILES['course_image']
        file_name = request.FILES['course_image'].name

        fs = FileSystemStorage() 
        file = fs.save(course_image.name, course_image)
        fileurl = fs.url(file)
        report = file_name

        Course.objects.filter(pk = id).update(course_image = course_image)
        messages.success(request, "Your course file has been updated successfully!")
        ur = Course.objects.get(pk=id)
        # form = CenterRoutineForm(instance=ur) 
        return redirect(add_course)
    else: 
        return render(request, 'update_course.html', {'id':id})   
