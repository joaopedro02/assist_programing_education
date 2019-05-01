from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Turmas(models.Model):
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    


class perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    turma = models.ForeignKey(
        Turmas,
        on_delete=models.CASCADE,
    )