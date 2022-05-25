from django import forms 
from .models import Provided_Content

class Provide_Content_Form(forms.ModelForm):
    class Meta:
        model = Provided_Content
        fields = '__all__'

