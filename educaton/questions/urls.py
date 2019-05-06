from django.urls import path

from . import views

app_name='questions'
urlpatterns = [
    path('form1/',views.form1,name='form1'),
    path('form2/',views.form2,name='form2'),
    path('resposta/',views.resposta,name='resposta'),
    path('respondido/',views.respondido,name='respondido'),
   
]
