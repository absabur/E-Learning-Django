from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from App_Student.forms import *
from App_Teacher.forms import *

from django.utils import timezone
from datetime import datetime

# Create your views here.
@login_required
def questions(request):
    questionForm = QuestionFrom()
    answerForm = QuestionAnswerForm()
    if request.method == 'POST':
        questionForm = QuestionFrom(request.POST)
        answerForm = QuestionAnswerForm(request.POST)
        if 'post_question' in request.POST:
            if questionForm.is_valid():
                ques = questionForm.save(commit=False)
                ques.user = request.user
                ques.save()
                messages.info(request,"Question Added!")
                return redirect('App_Student:questions')
        else:
            if answerForm.is_valid():
                ans = answerForm.save(commit=False)
                ans.user = request.user
                pk = int(request.POST.get('question_id'))
                ques = Question.objects.get(pk=pk)
                ans.question = ques
                ans.save()
                messages.info(request,"Answer Submitted!")
                return redirect('App_Student:questions')
    questions = Question.objects.all()
    return render(request, 'App_Student/questions.html', context={"questionForm": questionForm, 'answerForm': answerForm, 'questions': questions})
    



@login_required
def question_edit(request, pk):
    title = "Question"
    question = Question.objects.get(pk=pk, user=request.user)
    form = QuestionFrom(instance=question)
    if request.method == 'POST':
        form = QuestionFrom(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.info(request,"Question Updated!")
            return redirect('App_Student:questions')
    return render(request, 'App_Teacher/quiz_edit.html', context={'form': form, 'title': title})

@login_required
def question_delete(request, pk):
    question = Question.objects.get(pk=pk, user=request.user)
    question.delete()
    messages.warning(request,"Question Deleted!")
    return redirect('App_Student:questions')

@login_required
def answer_edit(request, pk):
    title = "Answer"
    answre = Answer.objects.get(pk=pk, user=request.user)
    form = AnswerForm(instance=answre)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answre)
        if form.is_valid():
            form.save()
            messages.info(request,"Answer Updated!")
            return redirect('App_Student:questions')
    return render(request, 'App_Teacher/quiz_edit.html', context={'form': form, 'title': title})

@login_required
def answer_delete(request, pk):
    answer = Answer.objects.get(pk=pk, user=request.user)
    answer.delete()
    messages.warning(request,"Answer Deleted!")
    return redirect('App_Student:questions')


@login_required
def quiz_results(request):
    answers = AnswerList.objects.filter(user=request.user)
    lists = []
    for answer in answers:
        quiz = Quiz.objects.get(id=answer.quiz.id)
        date_time_end = datetime.strptime(str(quiz.end_on), '%Y-%m-%d %H:%M:%S%z')
        if date_time_end < timezone.now():
            lists.append({"quiz": quiz, "answer": answer})
    return render(request, 'App_Student/quiz_results.html', context={"lists": lists})