from django.db import models
from django.utils import timezone

class Instructor(models.Model): 
    instructor_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    study_center = models.CharField(max_length=3)
    default_pass =models.CharField(max_length=100, default="DCSA")  
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.study_center+ "-" + self.name


class Assign_Course(models.Model): 
    assigned_course_id = models.AutoField(primary_key=True)
    study_center = models.CharField(max_length=3)
    instructor_id = models.CharField(max_length=15)
    assign_course = models.CharField(max_length=100)
    term = models.IntegerField()
    year =models.CharField(max_length=100, default="1st Semester")  
     
    def __str__(self):
        return self.study_center + " : " + self.instructor_id + " - " + self.assign_course
    
class Provided_Content(models.Model): 
    provided_content_id = models.AutoField(primary_key=True) 
    term = models.IntegerField()
    instructor_id = models.CharField(max_length=15)
    assigned_course = models.CharField(max_length=100) 
    content_title = models.CharField(max_length=20)
    content_desc = models.CharField(max_length=200)
    content_file = models.FileField(upload_to='content/file', default="", null=True, blank=True)
    
     
    def __str__(self):
        return self.instructor_id + " - " + self.content_title
    
class Tutor_Marks_Assignment(models.Model): 
    tma_id = models.AutoField(primary_key=True) 
    term = models.IntegerField()
    instructor_id = models.CharField(max_length=15)
    assigned_course = models.CharField(max_length=100) 
    tma_title = models.CharField(max_length=20)
    tma_desc = models.CharField(max_length=200)
    tma_file = models.FileField(upload_to='TMA/file', default="", null=True, blank=True)
    tma_date = models.DateField(default=timezone.now)
    tma_status = models.BooleanField(default=False)
    
    class Meta:
        unique_together = [['term', 'instructor_id', 'assigned_course']]

    def __str__(self):
        return self.instructor_id + " - " + self.tma_title    

class Tutor_Marks_Assignment2(models.Model): 
    tma_id = models.AutoField(primary_key=True) 
    term = models.IntegerField()
    instructor_id = models.CharField(max_length=15)
    assigned_course = models.CharField(max_length=100) 
    tma_title = models.CharField(max_length=20)
    tma_desc = models.CharField(max_length=200)
    tma_file = models.FileField(upload_to='TMA/file', default="", null=True, blank=True)
    tma_date = models.DateField(default=timezone.now)
    tma_status = models.BooleanField(default=False)
    
    class Meta:
        unique_together = [['term', 'instructor_id', 'assigned_course']]

    def __str__(self):
        return self.instructor_id + " - " + self.tma_title  
