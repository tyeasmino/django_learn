from django.contrib import admin

# Register your models here.
from .models import Course, Contact 

admin.site.register(Course)
admin.site.register(Contact)