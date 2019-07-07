from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import Cadastro_usuario
from django.contrib.auth.models import User
from django.contrib.auth import logout
from autentication.models import perfil
from django.views.generic import TemplateView


class Cadastro(FormView):
    template_name = 'cadastro/cadastro.html'
    form_class = Cadastro_usuario
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        email=form.cleaned_data['email']
        user=User.objects.create_user(username, email, password)
        user.first_name=form.cleaned_data['first_name']
        user.last_name=form.cleaned_data['last_name']
        user.save()
        p1=perfil(user=user,int_verbal_linguistica=0.0,int_musical=0.0,int_logico_matematica=0.0,int_cinestesico_corporal=0.0,int_espacial_visual=0.0,int_intrapessoal=0.0,int_naturalista=0.0,int_interpessoal=0.0,ea_ativo=0.0,ea_reflexivo=0.0,ea_pragmatico=0.0,ea_teorico=0.0)
        p1.save()
        return super().form_valid(form)

class Termo(TemplateView):
        template_name="cadastro/termo.html"

def logout_view(request):
    logout(request)
    return redirect('/home/')