from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from .models import Question,Answers
from django.template import loader
from django.urls import reverse

def index(request):
    questions=Question.objects.order_by('-question_text')
    context = {
        'questions':questions,
    }
    return render(request,'questions/index.html',context)

def resposta(request):
    
    return HttpResponseRedirect(reverse('questions:respondido'))

def respondido(request):
    context={
    }
    return render(request,'questions/respondido.html',context)
