from django import forms

class Cadastro_usuario(forms.Form):
    nome=forms.CharField(label="Nome",max_length=100)
    sobrenome=forms.CharField(label="Sobrenome",max_length=100)
    email=forms.EmailField(max_length=200)
    username=forms.TextInput()
    e_professor=forms.CheckboxInput()

