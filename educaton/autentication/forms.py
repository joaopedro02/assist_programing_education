from django import forms
from django.contrib.auth.models import User

class Cadastro_usuario(forms.Form):
    class meta:
        model=User
    # nome=forms.CharField(label="Nome",max_length=100)
    # sobrenome=forms.CharField(label="Sobrenome",max_length=100)
    # email=forms.EmailField(max_length=200)
    # username=forms.CharField(label="Usuário",max_length=100)
    # # senha=forms.PasswordInput()
    # sou_professor=forms.BooleanField(required=False)
    # concordo_com_os_termos=forms.BooleanField()


