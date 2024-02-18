from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from App_Teacher.forms import *
from App_Auth.models import UserProfile

from django.utils import timezone
from datetime import datetime
# Create your views here.
@login_required
def artcle_write(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    if not request.user.user_profile.role == 'teacher':
        messages.warning(request,"Only Teacher Can Access This Page!")
        return redirect('home')
    article = Article.objects.get(pk=pk, user=request.user)
    print(article.image)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request,"Article Updated Successfully!")
            return redirect('home')
    return render(request, 'App_Teacher/write_article.html',context={'form': form, 'image': article.image})


@login_required
def delete_aritcle(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    if not request.user.user_profile.role == 'teacher':
        messages.warning(request,"Only Teacher Can Access This Page!")
        return redirect('home')
    article = Article.objects.get(pk=pk, user=request.user)
    article.delete()
    messages.warning(request,"Article Deleted!")
    return redirect('home')

@login_required
def articles(request):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    articles = Article.objects.all()
    commentForm = CommentForm()
    replayForm = replayFrom()
    postForm = ArticleForm()
    if request.method == 'POST':
        if 'post_article' in request.POST:
            if not request.user.user_profile.role == 'teacher':
                messages.warning(request,"Only Teacher Can Access This Page!")
                return redirect('home')
            postForm = ArticleForm(request.POST, request.FILES)
            if postForm.is_valid():
                data = postForm.save(commit=False)
                data.user = request.user
                data.save()
                messages.success(request,"Article Posted Successfully!")
                return redirect('home')
        else:
            commentForm = CommentForm(request.POST)
            replayForm= replayFrom(request.POST)
            if commentForm.is_valid():
                data = commentForm.save(commit=False)
                data.user = request.user
                pk = int(request.POST.get('article_id'))
                article = Article.objects.get(pk=pk)
                data.article = article
                data.save()
                messages.info(request,"Comment Submitted!")
                return redirect('home')
            if replayForm.is_valid():
                data = replayForm.save(commit=False)
                article_id = int(request.POST.get('article_id'))
                comment_id = int(request.POST.get('comment_id'))
                article = Article.objects.get(pk=article_id)
                comment = Comment.objects.get(pk=comment_id)
                data.user = request.user
                data.article = article
                data.comment = comment
                messages.info(request,"Reply Submitted!")
                data.save()
                return redirect('home')
        
    return render(request, 'App_Teacher/articles.html', context={'articles': articles, 'commentForm': commentForm, 'replayForm': replayForm, "postForm": postForm})


@login_required
def liked_article(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    article = Article.objects.get(pk=pk)
    is_liked = Likes.objects.filter(user=request.user, article=article)
    if is_liked.exists():
        is_liked.delete()
        messages.warning(request,"Unliked!")
    else:
        Likes.objects.create(user=request.user, article=article)
        messages.success(request,"Liked!")
    return redirect('home')


@login_required
def quiz(request):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    quizzes = Quiz.objects.all()
    filtered_quiz = []
    if request.user.user_profile.role == 'teacher':
        filtered_quiz = list(quizzes)
    else:
        for quiz in quizzes:
            date_time_start = datetime.strptime(str(quiz.start_on), '%Y-%m-%d %H:%M:%S%z')
            date_time_end = datetime.strptime(str(quiz.end_on), '%Y-%m-%d %H:%M:%S%z')
            answer = AnswerList.objects.filter(quiz=quiz, user=request.user)
            if not answer and date_time_start <= timezone.now():
                if date_time_end > timezone.now():
                    filtered_quiz.append(quiz)
    form = QuizForm()
    answerForm = AnswerForm()
    if request.method == 'POST':
        if 'quiz_answer_quiz' in request.POST:
            answerForm = AnswerForm(request.POST)
            if answerForm.is_valid():
                data = answerForm.save(commit=False)
                quiz = int(request.POST.get('quiz_id'))
                quiz = Quiz.objects.get(pk=quiz)
                already_answer = AnswerList.objects.filter(quiz=quiz, user=request.user)
                if already_answer:
                    messages.warning(request, "Answer Already Submitted")
                    return redirect('App_Teacher:quiz')
                date_time_end = datetime.strptime(str(quiz.end_on), '%Y-%m-%d %H:%M:%S%z')
                if date_time_end < timezone.now():
                    messages.warning(request, "Time is up!")
                    return redirect('App_Teacher:quiz')
                data.user = request.user
                data.quiz = quiz
                data.save()
                messages.success(request,"Answer Submitted!")
                return redirect('App_Teacher:quiz')
        form = QuizForm(request.POST)
        if form.is_valid():
            if not request.user.user_profile.role == 'teacher':
                messages.warning(request,"Only Teacher Can Access This Page!")
                return redirect('home')
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request,"Quiz Added!")
            return redirect('App_Teacher:quiz')
    return render(request, 'App_Teacher/quiz.html', context={'quizzes': filtered_quiz, 'form': form, 'answerForm': answerForm})


@login_required
def quiz_edit(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    if not request.user.user_profile.role == 'teacher':
        messages.warning(request,"Only Teacher Can Access This Page!")
        return redirect('home')
    title = "Quiz"
    quiz = Quiz.objects.get(pk=pk, user=request.user)
    form = QuizForm(instance=quiz)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request,"Quiz Updated!")
            return redirect('App_Teacher:quiz')
    return render(request, 'App_Teacher/quiz_edit.html', context={'form': form, 'title': title})

@login_required
def quiz_delete(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    if not request.user.user_profile.role == 'teacher':
        messages.warning(request,"Only Teacher Can Access This Page!")
        return redirect('home')
    quiz = Quiz.objects.get(pk=pk, user=request.user)
    messages.warning(request,"Quiz Deleted!")
    quiz.delete()
    return redirect('App_Teacher:quiz')


@login_required
def comment_edit(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    title = "Comment"
    comment = Comment.objects.get(pk=pk, user=request.user)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.info(request,"Comment Updated!")
            return redirect('home')
    return render(request, 'App_Teacher/quiz_edit.html', context={'form': form, 'title': title})

@login_required
def comment_delete(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    comment = Comment.objects.get(pk=pk, user=request.user)
    comment.delete()
    messages.warning(request,"Comment Deleted!")
    return redirect('home')

@login_required
def reply_edit(request, pk):
    userinfo = UserProfile.objects.filter(user=request.user)
    if not userinfo:
        messages.warning(request,"Add your information first!")
        return redirect('App_Auth:userInfo')
    title = "Comment"
    comment = Replay.objects.get(pk=pk, user=request.user)
    form = replayFrom(instance=comment)
    if request.method == 'POST':
        form = replayFrom(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request,"Reply Updated!")
            return redirect('home')
    return render(request, 'App_Teacher/quiz_edit.html', context={'form': form, 'title': title})

@login_required
def reply_delete(request, pk):
    comment = Replay.objects.get(pk=pk, user=request.user)
    comment.delete()
    messages.warning(request,"Reply Deleted!")
    return redirect('home')



