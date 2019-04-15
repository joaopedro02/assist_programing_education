from django.shortcuts import render
from django.http import HttpResponse
from .models import Question,Answers
from django.template import loader

def index(request):
    questions=Question.objects.order_by('-question_text')
    #output = ', '.join([q.question_text for q in questions])
    #template=loader.get_template('questions/index.html')
    context = {
        'questions':questions,
    }
    return render(request,'questions/index.html',context)
# Create your views here.
