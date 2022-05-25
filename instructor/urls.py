from django.urls import path 
from . import views

urlpatterns = [    
    path("add_instructor/", views.add_instructor, name="add_instructor"),  
    path("assign_course/", views.assign_course, name="assign_course"),  
]