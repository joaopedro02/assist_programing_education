import pygal
from django.contrib.auth.models import User
from autentication.models import perfil 

class BarChart_estAprendizagem():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        
    def set_title(self):
        self.chart.title = 'Estilos de aprendizagem'

    def get_data(self, request):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        
        data = {"Ativo":request.user.perfil.ea_ativo,"Reflexivo":request.user.perfil.ea_reflexivo,"Pragmático":request.user.perfil.ea_pragmatico,"Teórico":request.user.perfil.ea_teorico}
        
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