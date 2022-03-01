from django.contrib import admin
from .forms import CenterCreateForm

# Register your models here.
from .models import StudyCenter, Semester, CourseSemseter, BookTitle, Book, Routine

admin.site.register(StudyCenter)
admin.site.register(Semester)
admin.site.register(CourseSemseter)
admin.site.register(BookTitle)
admin.site.register(Book)
admin.site.register(Routine)