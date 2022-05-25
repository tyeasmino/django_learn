from django.urls import path 
from . import views

urlpatterns = [    
    path("add_learner/", views.add_learner, name="add_learner"),  
]