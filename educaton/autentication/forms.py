from django import forms
from django.contrib.auth.models import User

class Cadastro_usuario(forms.ModelForm):

    concordo_com_os_termos=forms.BooleanField()
    class Meta:
        model=User
        fields = ['first_name','last_name','email','username','password']
        widgets = {'password': forms.PasswordInput}
    # nome=forms.CharField(label="Nome",max_length=100)
    # sobrenome=forms.CharField(label="Sobrenome",max_length=100)
    # email=forms.EmailField(max_length=200)
    # username=forms.CharField(label="Usuário",max_length=100)
    # senha=forms.CharField(label="Senha",max_length=80)
    # sou_professor=forms.BooleanField(required=False)
    


