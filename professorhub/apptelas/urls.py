from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('disciplinas/', disciplinas_view, name='disciplinas'),
    path('tarefas/', tarefas_view, name='tarefas'),
    path('avaliacoes/', avaliacoes_view, name='avaliacoes'),

    path('disciplinas/<int:id>/', disciplina_detail_view, name='disciplina_detail'),

    path('configuracoes/', configuracoes_view, name='configuracoes'),
    
    path('calendarios/', calendarios_view, name='calendario'),
    path('calendarios/<int:id>/', calendario_detail_view, name='calendario_detail'),

    path('enviar-email', enviar_email_verificacao_view, name='enviar_email_verificacao'),
    path('conta-ativada', conta_ativada_view, name='conta_ativada')
]
