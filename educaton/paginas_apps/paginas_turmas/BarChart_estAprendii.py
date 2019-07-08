import pygal
from django.contrib.auth.models import User
from autentication.models import perfil 

class BarChart_estAprendizagem():

    def __init__(self, **kwargs):
        self.chart = pygal.Bar(**kwargs)
        
    def set_title(self,titulo):
        self.chart.title = titulo

    def get_data(self, ea_ativo, ea_reflexivo, ea_pragmatico, ea_teorico):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        
        data = {"Ativo":ea_ativo,"Reflexivo":ea_reflexivo,"Pragmático":ea_pragmatico,"Teórico":ea_teorico}
        
        return data

    def generate(self,ea_ativo, ea_reflexivo, ea_pragmatico, ea_teorico):
        # Get chart data
        chart_data = self.get_data(ea_ativo, ea_reflexivo, ea_pragmatico, ea_teorico)

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)
        self.chart.value_formatter = lambda x: "%.1f%%" % x
        # Return the rendered SVG
        return self.chart.render(is_unicode=True)