from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=400)
    form = models.IntegerField(default=0)

class Answers(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    answers_text=models.CharField(max_length=400)
    answers_value=models.IntegerField(default=0)

# Create your models here.
