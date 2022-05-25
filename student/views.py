from django.shortcuts import render
from django.contrib import messages
from .models import Learner
import csv, io 
from account.models import User 
# Create your views here.

def add_learner(request):
    learner = Learner.objects.all()
    template = "add_learner.html"

    context = {
        "learner": learner,  
    }

    if request.method == "GET": 
        return render(request, template, context)

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar='|'):
        _, created = Learner.objects.update_or_create(
            learner_id = column[0],
            name = column[1],
            father_name = column[2],
            study_center = column[3],
            semester_01 = column[4],
            semester_02 = column[5],
            semester_03 = column[6],
            default_pass = column[7],
        ) 

        user = User()
        user.username = column[0]
        user.first_name = column[1]
        user.set_password(column[7])  
        user.is_active = True 
        user.is_learner = True 
        user.save() 

    messages.success(request, "Learner has been added successfully!")
    return render(request, template, context)

    # 
    # form = csvModelForm(request.POST or None, request.FILES or None)

    
    # if form.is_valid():
    #     form.save()
    #     form = csvModelForm()
    #     obj = CSV.objects.get(activated=False)

    #     with open(obj.file_name.path, 'r') as f: 
    #         reader = csv.reader(f)

    #         for i, row in enumerate(reader):
    #             if i==0:
    #                 pass 
    #             else:  
    #                 row = "".join(row)
    #                 row = row.replace(";", "")
    #                 row = row.split()
                    
    #                 student_id = row[0]
    #                 name = row[1].upper()
    #                 father_name = row[2].upper()
    #                 study_center = row[3]
    #                 default_pass = row[4]

    #                 user = User()
    #                 user.username = row[0]
    #                 user.first_name = row[1]
    #                 user.set_password(row[4])
    #                 user.is_active = True
    #                 user.is_learner = True
    #                 user.save() 

    #                 Student.objects.create(
    #                     student_id= student_id,
    #                     name = name,
    #                     father_name = father_name, 
    #                     study_center= study_center,
    #                     default_pass= default_pass
    #                 )
    #         obj.activated = True 
    #         obj.save() 
    #         messages.success(request, "Your CSV file and Learner has been added successfully!")
    # context = {
    #     "form": form,      
    #     "learner": learner,  
    # }
    # return render(request,'add_learner.html', context)


 
# Final code of last time: 
# learner = Student.objects.all()
#     template = "add_learner.html"

#     context = {
#         "learner": learner,  
#     }

#     if request.method == "GET": 
#         return render(request, template, context)

#     csv_file = request.FILES['file']

#     data_set = csv_file.read().decode('UTF-8')
#     io_string = io.StringIO(data_set)
#     next(io_string)
#     for column in csv.reader(io_string, delimiter=',', quotechar='|'):
#         _, created = Student.objects.update_or_create(
#             student_id = column[0],
#             name = column[1],
#             father_name = column[2],
#             study_center = column[3],
#             default_pass = column[4],
#         ) 

#         user = User()
#         user.username = column[0]
#         user.first_name = column[1]
#         user.set_password(column[4])  
#         user.is_active = True 
#         user.is_learner = True 
#         user.save() 

#     messages.success(request, "Learner has been added successfully!")
#     return render(request, template, context)