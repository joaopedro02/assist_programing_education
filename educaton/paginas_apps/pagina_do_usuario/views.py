from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from questions.models import Answers
from .BarChart_intMultiplas import BarChart
from pygal.style import BlueStyle
from .BarChart_estAprendi import BarChart_estAprendizagem

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