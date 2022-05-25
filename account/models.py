from django.db import models
from django.contrib.auth.models import AbstractUser
from StudyCenter.models import StudyCenter
from course.models import Course
# Create your models here.


class User(AbstractUser): 
    is_admin = models.BooleanField('Is Admin', default=False)
    is_learner = models.BooleanField('Is Learner', default=False)
    is_instructor = models.BooleanField('Is Instructor', default=False)

class User_Detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_Number = models.IntegerField()
    user_Profile = models.ImageField(upload_to="user/profile", default="user/profile/user.png", null=True)
    user_course = models.ForeignKey(Course, on_delete=models.CASCADE)   
    # user_Study_Center = models.ForeignKey(StudyCenter, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 