from django import forms
from .models import AppUser,Task

class UserForm(forms.ModelForm):
    class Meta:
        model=AppUser
        fields=['username','password','email']

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)
    
