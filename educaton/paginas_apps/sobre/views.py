from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import RedirectView

# Create your views here.
class sobre(TemplateView):
    template_name="sobre/sobre.html"

