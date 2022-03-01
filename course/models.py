from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField 
    course_name = models.CharField(max_length=50) 
    course_designed_by = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=70, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500)
    release_date = models.DateField(default=timezone.now)
    course_price = models.IntegerField(default=0)
    course_image = models.ImageField(upload_to="course/image", default="")
    course_aim1 = models.CharField(max_length=200, default="", blank=True)
    course_aim2 = models.CharField(max_length=200, default="", blank=True)
    course_aim3 = models.CharField(max_length=200, default="", blank=True)
    course_aim4 = models.CharField(max_length=200, default="", blank=True)
    course_aim5 = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return self.course_name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50) 
    contact_email = models.CharField(max_length=100, default="")
    contact_phone = models.CharField(max_length=20, default="")
    contact_desc = models.CharField(max_length=500, default="")

    def __str__(self): 
        return self.contact_name

