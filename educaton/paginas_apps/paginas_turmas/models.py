from django.db import models
from django.contrib.auth.models import User

class Turmas(models.Model):
    nome=models.CharField(max_length=200)
    cor=models.CharField(max_length=100)
    descricao=models.CharField(max_length=1000)
    
    alunos=models.ManyToManyField(User,related_name='turmas_onde_sou_aluno')
    mestres=models.ManyToManyField(User,related_name='turmas_onde_sou_mestre')

