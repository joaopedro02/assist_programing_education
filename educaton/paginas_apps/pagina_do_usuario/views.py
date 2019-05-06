from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.models import Answers

class pagina_inicial(LoginRequiredMixin,TemplateView):
    template_name="pagina_do_usuario/pagina_do_usuario.html"
    
    def get_context_data(self, **kwargs):
        answer=Answers.objects.filter(user__username=self.request.user.get_username())
        countanswer1=int(answer.filter(question__form=1).count())# estilos de aprendizagem
        countanswer2=int(answer.filter(question__form=2).count())# inteligencias multiplas
        print(countanswer1)
        print(countanswer2)
        context = super(pagina_inicial, self).get_context_data(**kwargs)
        context.update({'countanswer2':countanswer2,'countanswer1':countanswer1})
        return context