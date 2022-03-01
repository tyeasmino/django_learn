from django.db import models
from course.models import Course 

class StudyCenter(models.Model):
    s_course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    studyCenter_code = models.CharField(max_length=3, primary_key=True)
    studyCenter_name = models.CharField(max_length=100)
    studyCenter_location = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.studyCenter_code


class Semester(models.Model):
    semester_id = models.AutoField
    semester_name = models.CharField(max_length=50, default="", null=True)

    def __str__(self):
        return self.semester_name


class CourseSemseter(models.Model):
    s_course_name =  models.ForeignKey(Course, on_delete=models.CASCADE)
    s_course_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

class BookTitle(models.Model):
    title_id = models.AutoField
    book_title = models.CharField(max_length=100, default="")
    book_img = models.ImageField(upload_to='book/img', default="")

    def __str__(self):
        return self.book_title
        
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    book_semester_name = models.ForeignKey(Semester, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100, default="")
    book_unit_no = models.CharField(max_length=30, default="")
    book_unit_name = models.CharField(max_length=100, default="")
    book_unit_page = models.CharField(max_length=10, default="")
    book_file = models.FileField(upload_to='book/file', default="", null=True, blank=True)

    def __str__(self):
        return self.book_title + " : " + self.book_unit_no + " :: " + self.book_unit_name 

class Routine(models.Model):
    routine_id = models.AutoField(primary_key=True)
    routine_of_the_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    routine_name = models.CharField(max_length=200, default="")
    routine_file = models.FileField(upload_to='routine')

    def __str__(self):
        return self.routine_name 


