from django import forms
from django.contrib.auth.models import User
from .models import *



class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['roll_no','name','class_name','school_name','mobile_number','address']


class StudentAcademicsForm(forms.ModelForm):
    class Meta:
        model = StudentAcademics
        fields = ['student','maths','physics','chemistry','biology','english']


class StudentInfoFormNew(forms.Form):
    name = forms.CharField(max_length=100,required =True)
    class_name = forms.CharField(max_length=100,required =True)
    school_name = forms.CharField(max_length=100,required =True)
    mobile_number = forms.CharField(max_length=100,required =True)
    address = forms.CharField(max_length=500,required =True)
    maths = forms.IntegerField(required =True)
    physics = forms.IntegerField(required =True)
    chemistry = forms.IntegerField(required =True)
    biology = forms.IntegerField(required =True)
    english = forms.IntegerField(required =True)


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password', 'email', 'first_name','last_name']
