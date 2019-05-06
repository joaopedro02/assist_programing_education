from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=400)
    form = models.IntegerField(default=0)
    number= models.IntegerField(default=0)
    
    def __str__(self):
        return self.question_text

class Answers(models.Model):
    user=models.ManyToManyField(User)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    answers_value=models.IntegerField(default=0)

    def __str__(self):
        return str(self.answers_value)

# class User_answers(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     answers=models.ForeignKey(Answers,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.answers +" "+ self.user
# Create your models here.
