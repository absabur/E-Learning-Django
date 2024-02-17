from django import forms
from django.contrib.auth.models import User

from App_Student.models import *


class QuestionFrom(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("content",)
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Ask a question',  'class':"post-area"}),
        }
        
        
class QuestionAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ("content",)
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Answer this question'}),
        }
