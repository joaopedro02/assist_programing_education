from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import Cadastro_usuario
from django.contrib.auth.models import User


class Cadastro(CreateView):
    template_name = 'cadastro/cadastro.html'
    model=User
    fields = ['first_name','last_name','email','username','password']
    # form_class = Cadastro_usuario
    success_url = '#'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.

    #     return super().form_valid(form)
