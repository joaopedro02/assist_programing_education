
from django.contrib import auth
from django.urls import path,include
from . import views

app_name='autentication'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]