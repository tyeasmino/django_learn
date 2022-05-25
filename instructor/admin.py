from django.contrib import admin
from .models import Instructor, Assign_Course, Provided_Content, Tutor_Marks_Assignment, Tutor_Marks_Assignment2
# Register your models here.

admin.site.register(Instructor)
admin.site.register(Assign_Course)
admin.site.register(Provided_Content)
admin.site.register(Tutor_Marks_Assignment)
admin.site.register(Tutor_Marks_Assignment2)
