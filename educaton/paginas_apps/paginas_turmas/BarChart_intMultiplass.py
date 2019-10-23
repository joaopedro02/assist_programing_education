import pygal
from django.contrib.auth.models import User
from autentication.models import perfil 

class BarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        
    def set_title(self,titulo):
        self.chart.title = titulo

    def get_data(self, int_verbal_linguistica,int_musical,int_logico_matematica,int_cinestesico_corporal,int_espacial_visual,int_intrapessoal,int_naturalista,int_interpessoal):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        
        data = {"Verbal Linguística":int_verbal_linguistica,"Musical":int_musical,"Lógico mátematica":int_logico_matematica,"Cinestésico corporal":int_cinestesico_corporal,"Espacial visual":int_espacial_visual,"Intrapessoal":int_intrapessoal,"Naturalista":int_naturalista,"Interpessoal":int_interpessoal}
        
        return data

    def generate(self, int_verbal_linguistica,int_musical,int_logico_matematica,int_cinestesico_corporal,int_espacial_visual,int_intrapessoal,int_naturalista,int_interpessoal):
        # Get chart data
        chart_data = self.get_data(int_verbal_linguistica,int_musical,int_logico_matematica,int_cinestesico_corporal,int_espacial_visual,int_intrapessoal,int_naturalista,int_interpessoal)

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)
        self.chart.value_formatter = lambda x: "%.1f%%" % x
        # Return the rendered SVG
        return self.chart.render(is_unicode=True)