from django.db import models
from django.utils import timezone

class Student(models.Model): 
    student_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    study_center = models.CharField(max_length=3)
    semester_01 = models.BooleanField(default=True)
    semester_02 = models.BooleanField(default=False)
    semester_03 = models.BooleanField(default=False)
    default_pass =models.CharField(max_length=100, default="DCSA")  
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.student_id 
    
class Learner(models.Model):
    learner_id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    study_center = models.CharField(max_length=3)
    semester_01 = models.IntegerField(blank=False, null=False)
    semester_02 = models.IntegerField(default="0", blank=True, null=True)
    semester_03 = models.IntegerField(default="0", blank=True, null=True)
    default_pass = models.CharField(max_length=100, default="DCSA")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.learner_id
    
   
class Learner_Submit_TMA1(models.Model): 
    tma_id = models.AutoField(primary_key=True) 
    term = models.IntegerField()
    learner_id = models.CharField(max_length=15)
    assigned_course = models.CharField(max_length=100)  
    tma_file = models.FileField(upload_to='Learner_TMA/file', default="", null=True, blank=True)
    tma_date = models.DateField(default=timezone.now)
    tma_status = models.BooleanField(default=False)
    
    class Meta:
        unique_together = [['term', 'learner_id', 'assigned_course']]

    def __str__(self):
        return self.learner_id + " - " + self.assigned_course  

class Learner_Submit_TMA2(models.Model): 
    tma_id = models.AutoField(primary_key=True) 
    term = models.IntegerField()
    learner_id = models.CharField(max_length=15) 
    assigned_course = models.CharField(max_length=100)  
    tma_file = models.FileField(upload_to='Learner_TMA/file', default="", null=True, blank=True)
    tma_date = models.DateField(default=timezone.now)
    tma_status = models.BooleanField(default=False)
    
    class Meta:
        unique_together = [['term', 'learner_id', 'assigned_course']]

    def __str__(self):
        return self.learner_id + " - " + self.assigned_course  
