from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-updated_at', '-created_at', 'title']
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
    class Meta:
        ordering = ['-updated_at', '-created_at',]

class Replay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    replay = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.replay
    class Meta:
        ordering = [ 'created_at', 'updated_at',]
        verbose_name_plural = 'Replies'
        
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at',]
        
        
class Quiz(models.Model):
    answer_list= [
        ('', 'Select Correct Answer'),
        ('option_1', '(A)'),
        ('option_2', '(B)'),
        ('option_3', '(C)'),
        ('option_4', '(D)'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField(max_length=500)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=15, choices=answer_list)
    
    start_on = models.DateTimeField()
    end_on = models.DateTimeField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question
    class Meta:
        ordering = ['-updated_at', '-created_at', 'question']
    

class AnswerList(models.Model):
    answer_list= [
        ('', 'Select Correct Answer'),
        ('option_1', '(A)'),
        ('option_2', '(B)'),
        ('option_3', '(C)'),
        ('option_4', '(D)'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer = models.CharField(max_length=15, choices=answer_list)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.answer