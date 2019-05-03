from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Turmas(models.Model):
    nome=models.CharField(max_length=100)
    


class perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(
        Turmas,
        on_delete=models.CASCADE,
    )
    