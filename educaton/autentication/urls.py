
from django.contrib import auth
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


app_name='autentication'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view() ,name='login'),
    path('logout/',views.logout_view ,name='logout'),
    path('cadastrar/', views.Cadastro.as_view(),name='cadastrar'),
    path('profile/',include('paginas_apps.pagina_do_usuario.urls')),
]