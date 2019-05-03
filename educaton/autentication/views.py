from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views.generic.edit import FormView
from autentication.forms import Cadastro_usuario

class Cadastro(FormView):
    template_name = 'cadastro/cadastro.html'
    form_class = Cadastro_usuario
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)
