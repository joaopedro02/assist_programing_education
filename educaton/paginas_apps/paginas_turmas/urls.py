"""educaton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from . import views
app_name='paginas_turmas'
urlpatterns = [
    path('',views.pagina_inicial.as_view(),name='pagina_inicial_turmas'),
    path('<int:turma_id>/',views.turma.as_view(),name='pagina_turma_especifica'),
    path('adicionar/',views.addturma,name='add_turma'),
    path('criar/', views.cria_turma.as_view(),name='cria_turma'),
]
