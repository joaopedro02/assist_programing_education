from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


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
    f_int=models.BooleanField(default=False)
    f_est=models.BooleanField(default=False)

    def __str__(self):
        return self.user
    
    