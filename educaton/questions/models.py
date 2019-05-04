from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=400)
    form = models.IntegerField(default=0)
    number= models.IntegerField(default=0)

class Answers(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    answers_value=models.IntegerField(default=0)

# Create your models here.
