from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.models import Answers
from .BarChart_intMultiplas import BarChart
from pygal.style import BlueStyle
from .BarChart_estAprendi import BarChart_estAprendizagem
from django.contrib.auth.models import User

from paginas_apps.paginas_turmas.BarChart_intMultiplass import BarChart as BarChart2
from paginas_apps.paginas_turmas.BarChart_estAprendii import BarChart_estAprendizagem as BarChart_estAprendizagem2 

class pagina_inicial(LoginRequiredMixin,TemplateView):
    template_name="pagina_do_usuario/pagina_do_usuario.html"
    
    def get_context_data(self, **kwargs):

        answer=Answers.objects.filter(user__username=self.request.user.get_username())
        countanswer1=int(answer.filter(question__form=1).count())# estilos de aprendizagem
        countanswer2=int(answer.filter(question__form=2).count())# inteligencias multiplas
        # print(countanswer1)
        # print(countanswer2)

        context = super(pagina_inicial, self).get_context_data(**kwargs)
        grafico_int = BarChart(
            print_zeroes=False,
            height=400,
            width=590,
            explicit_size=True,
            style=BlueStyle(
                  font_family='googlefont:Roboto',
                  value_colors=('black',)),
            show_y_guides=False,
            include_x_axis=False,
            print_values=True,
            print_values_position='top'
            
        )
        grafico_int.set_title()

        grafico_estilos=BarChart_estAprendizagem(
            print_zeroes=False,
            height=400,
            width=590,
            explicit_size=True,
            style=BlueStyle(
                  font_family='googlefont:Roboto',
                  value_colors=('black',)),
            show_y_guides=False,
            include_x_axis=False,
            print_values=True,
            print_values_position='top'
            
        )

        grafico_estilos.set_title()
        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        context.update({'countanswer2':countanswer2,'countanswer1':countanswer1})
        context['grafico_int'] = grafico_int.generate(self.request)
        context['grafico_estilos'] = grafico_estilos.generate(self.request)

        return context

class pagina_usuario_externa(LoginRequiredMixin,TemplateView):
    template_name="pagina_do_usuario/visao_externa.html"
    
    def get_context_data(self, **kwargs):
        id_usuario=kwargs['id_usuario']
        answer=Answers.objects.filter(user__id=id_usuario)
        countanswer1=int(answer.filter(question__form=1).count())# estilos de aprendizagem
        countanswer2=int(answer.filter(question__form=2).count())# inteligencias multiplas
        # print(countanswer1)
        # print(countanswer2)

        context = super(pagina_usuario_externa, self).get_context_data(**kwargs)
        grafico_int = BarChart2(
            # print_zeroes=False,
            # height=590,
            # width=590
            # explicit_size=True,
            # style=BlueStyle(
            #       font_family='googlefont:Roboto',
            #       value_colors=('black',)),
            # show_y_guides=False,
            # include_x_axis=False,
            # print_values=True,
            # print_values_position='top'
            
        )
        grafico_int.set_title('Inteligências múltiplas')

        grafico_estilos=BarChart_estAprendizagem2(
            print_zeroes=False,
            height=400,
            width=590,
            explicit_size=True,
            style=BlueStyle(
                  font_family='googlefont:Roboto',
                  value_colors=('black',)),
            show_y_guides=False,
            include_x_axis=False,
            print_values=True,
            print_values_position='top'
            
        )
        a=User.objects.filter(pk=id_usuario)[0]

        int_verbal=a.perfil.int_verbal_linguistica
        int_musical=a.perfil.int_musical
        int_logic=a.perfil.int_logico_matematica
        int_cinestesico=a.perfil.int_cinestesico_corporal
        int_espacial=a.perfil.int_espacial_visual
        int_intrapessoal=a.perfil.int_intrapessoal
        int_naturalista=a.perfil.int_naturalista
        int_interpessoal=a.perfil.int_interpessoal

        e_ativo=a.perfil.ea_ativo
        e_reflexivo=a.perfil.ea_reflexivo
        e_pragmatico=a.perfil.ea_pragmatico
        e_teorico=a.perfil.ea_teorico

        grafico_estilos.set_title('Estilos de aprendizagem')
        # Call the `.generate()` method on our chart object
        # and pass it to template context.
        
        context.update({'countanswer2':countanswer2,'countanswer1':countanswer1})
        context['t']=a
        context['grafico_int'] = grafico_int.generate(int_verbal, int_musical, int_logic, int_cinestesico, int_espacial, int_intrapessoal, int_naturalista, int_interpessoal)
        context['grafico_estilos'] = grafico_estilos.generate(e_ativo, e_reflexivo, e_pragmatico, e_teorico)

        return context
    pass