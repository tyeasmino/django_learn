from django import forms 
from .models import StudyCenter, Book, Routine

class CenterCreateForm(forms.ModelForm):
    class Meta:
        model = StudyCenter
        fields = ['s_course_name', 'studyCenter_code', 'studyCenter_name', 'studyCenter_location']

class CenterBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_course_name', 'book_semester_name', 'book_title', 'book_unit_no', 'book_unit_name', 'book_unit_page', 'book_file']

class CenterRoutineForm(forms.ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'