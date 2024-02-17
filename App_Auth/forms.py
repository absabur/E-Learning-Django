from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App_Auth.models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        

role_list= [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ]

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        labels = {
            'role': 'Choose Your Role',
            'id_number': 'Your ID',
            'image': 'Profile Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'id_number': forms.TextInput(attrs={'placeholder': 'Enter Your Id'}),
            'role': forms.RadioSelect(choices=role_list),
        }
        
        
class UserInfoChangeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','role')
        labels = {
            'id_number': 'Your ID',
            'image': 'Profile Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'id_number': forms.TextInput(attrs={'placeholder': 'Enter Your Id'}),
        }