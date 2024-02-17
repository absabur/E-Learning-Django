from django import forms
from django.contrib.auth.models import User
from App_Teacher.models import *



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user',)
        labels = {
            'title': '',
            'content': '',
            'image': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter article title',  'class':"post-title-input"}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter article title',  'class':"post-area"}),
        }
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write a comment'}),
        }
        
        
class replayFrom(forms.ModelForm):
    class Meta:
        model = Replay
        fields = ('replay',)
        labels = {
            'replay': '',
        }
        widgets = {
            'replay': forms.Textarea(attrs={'placeholder': 'Replay in this comment'}),
        }
        

    
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('question', 'option_1', 'option_2', 'option_3', 'option_4', 'answer', 'start_on', 'end_on')
        labels = {
            '': '',
        }
        widgets = {
            'start_on': forms.TextInput(attrs={'type': 'datetime-local',}),
            'end_on': forms.TextInput(attrs={'type': 'datetime-local',}),
        }
        
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerList
        fields = ('answer',)