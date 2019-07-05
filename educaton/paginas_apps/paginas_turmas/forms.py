from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Turmas

def validate_exists(value):
    try:
        t = Turmas.objects.get(pk=value)
    except Turmas.DoesNotExist:
        raise ValidationError(
            " Essa turma não existe"
        )


class Add_turma(forms.Form):

    cod_turma=forms.IntegerField(validators=[validate_exists])
    # class Meta:
    #     model=User
    #     fields = ['first_name','last_name','email','username','password']
    #     widgets = {'password': forms.PasswordInput}
    # # nome=forms.CharField(label="Nome",max_length=100)
    # sobrenome=forms.CharField(label="Sobrenome",max_length=100)
    # email=forms.EmailField(max_length=200)
    # username=forms.CharField(label="Usuário",max_length=100)
    # senha=forms.CharField(label="Senha",max_length=80)
    # sou_professor=forms.BooleanField(required=False)
    
class Cria_turma(forms.ModelForm):
    
    # star_color = forms.CharField(widget=ColorPickerWidget)
    class Meta:
        model=Turmas
        fields = ['nome','descricao']
        
