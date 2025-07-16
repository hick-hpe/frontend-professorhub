from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='apptelas/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('disciplinas/', disciplinas_view, name='disciplinas'),
    path('calendario/', calendarios_view, name='calendario'),
    path('tarefas/', tarefas_view, name='tarefas'),
    path('avaliacoes/', avaliacoes_view, name='avaliacoes'),
    path('planos-aula/', planos_aula_view, name='planos_aula'),
]
