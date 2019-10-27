import pygal
from django.contrib.auth.models import User
from autentication.models import perfil 
from pygal.style import BlueStyle

class BarChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Radar(height=400,width=400,style=BlueStyle(
                font_family='googlefont:Roboto',
                   value_colors=('black',)),show_legend=False,fill=True)
        
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
        nomes=[]
        valores=[]
        for key, value in chart_data.items():
            valores.append(value)
            nomes.append(key)
            #self.chart.add(key, value)
        # radar_chart = pygal.Radar()
        # radar_chart.title = 'V8 benchmark results'
        self.chart.x_labels = nomes
        self.chart.add('', valores)
        # radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
        # radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
        # radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
        self.chart.value_formatter = lambda x: "%.1f%%" % x
        # Return the rendered SVG
        return self.chart.render(is_unicode=True)