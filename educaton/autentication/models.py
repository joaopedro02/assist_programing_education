from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Turmas(models.Model):
    nome=models.CharField(max_length=100)
    alunos=models.ManyToManyField(User,related_name='turmas_onde_sou_aluno')
    professores=models.ManyToManyField(User,related_name='turmas_onde_sou_professor')


class perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    int_verbal_linguistica=models.FloatField()
    int_musical=models.FloatField()
    int_logico_matematica=models.FloatField()
    int_cinestesico_corporal=models.FloatField()
    int_espacial_visual=models.FloatField()
    int_intrapessoal=models.FloatField()
    int_naturalista=models.FloatField()
    int_interpessoal=models.FloatField()
    ea_ativo=models.FloatField()
    ea_reflexivo=models.FloatField()
    ea_pragmatico=models.FloatField()
    ea_teorico=models.FloatField()
    
    