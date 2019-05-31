import pygal
from django.contrib.auth.models import User
from autentication.models import perfil 

class BarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        
    def set_title(self):
        self.chart.title = 'Inteligências multiplas'

    def get_data(self, request):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        
        data = {"Verbal Linguística":request.user.perfil.int_verbal_linguistica,"Musical":request.user.perfil.int_musical,"Lógico mátematica":request.user.perfil.int_logico_matematica,"Cinestésico corporal":request.user.perfil.int_cinestesico_corporal,"Espacial visual":request.user.perfil.int_espacial_visual,"Intrapessoal":request.user.perfil.int_intrapessoal,"Naturalista":request.user.perfil.int_naturalista,"Interpessoal":request.user.perfil.int_interpessoal}
        
        return data

    def generate(self,request):
        # Get chart data
        chart_data = self.get_data(request)

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)
        self.chart.value_formatter = lambda x: "%.1f%%" % x
        # Return the rendered SVG
        return self.chart.render(is_unicode=True)