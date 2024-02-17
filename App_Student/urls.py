from django.urls import path
from App_Student.views import *

app_name = 'App_Student'

urlpatterns = [
    path('questions/', questions, name='questions'),
    path('question-edit/<pk>/', question_edit, name='question_edit'),
    path('question-delete/<pk>/', question_delete, name='question_delete'),
    path('answer-edit/<pk>/', answer_edit, name='answer_edit'),
    path('answer-delete/<pk>/', answer_delete, name='answer_delete'),
    path('quiz-results/', quiz_results, name='quiz_results'),
]
