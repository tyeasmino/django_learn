from django.contrib import admin
from .models import Student, Learner, Learner_Submit_TMA1, Learner_Submit_TMA2
# Register your models here.

admin.site.register(Student)
admin.site.register(Learner)
admin.site.register(Learner_Submit_TMA1)
admin.site.register(Learner_Submit_TMA2)

