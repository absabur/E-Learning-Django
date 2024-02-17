from django.urls import path
from App_Teacher.views import *

app_name = 'App_Teacher'

urlpatterns = [
    path('write-article/<pk>/', artcle_write, name='artcle_write'),
    path('delete-article/<pk>/', delete_aritcle, name='delete_aritcle'),
    path('liked-article/<pk>/', liked_article, name='liked_article'),
    path('articles/', articles, name='articles'),
    path('quiz/', quiz, name='quiz'),
    path('quiz-edit/<pk>/', quiz_edit, name='quiz_edit'),
    path('quiz-delete/<pk>/', quiz_delete, name='quiz_delete'),
    path('comment-edit/<pk>/', comment_edit, name='comment_edit'),
    path('comment-delete/<pk>/', comment_delete, name='comment_delete'),
    path('reply-edit/<pk>/', reply_edit, name='reply_edit'),
    path('reply-delete/<pk>/', reply_delete, name='reply_delete'),
]
