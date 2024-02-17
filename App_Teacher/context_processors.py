from App_Teacher.models import *
from App_Student.models import *
from django.utils import timezone
from datetime import datetime

def my_custom_data(request):
    my_data = {'content': ""}
    if request.user.is_authenticated:
        quizzes = Quiz.objects.all()
        questions = Question.objects.all()
        filtered_quiz = []
        for quiz in quizzes:
            date_time_start = datetime.strptime(str(quiz.start_on), '%Y-%m-%d %H:%M:%S%z')
            date_time_end = datetime.strptime(str(quiz.end_on), '%Y-%m-%d %H:%M:%S%z')
            answer = AnswerList.objects.filter(quiz=quiz, user=request.user)
            if not answer and date_time_start <= timezone.now():
                if date_time_end > timezone.now():
                    filtered_quiz.append(quiz)
        filtered_questions = []
        for question in questions:
            answer = Answer.objects.filter(question=question)
            if not answer:
                filtered_questions.append(question)
        my_data = {
            'quiz': len(filtered_quiz),
            'question': len(filtered_questions)
            # Add more data here as needed
        }
    return {'my_data': my_data}