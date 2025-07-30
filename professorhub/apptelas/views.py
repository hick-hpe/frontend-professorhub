from django.shortcuts import render, redirect
from .forms import UserRegister, UserLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login


def index_view(request):
    return render(request, 'apptelas/index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()

            # pagina de ativacao da conta
            return redirect('enviar_email_verificacao')
        
        return render(request, 'apptelas/register.html', {
            'form': form,
        })

    form = UserRegister()
    return render(request, 'apptelas/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = UserLogin(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()

            # Realiza o login
            login(request, user)
            return redirect("dashboard")
    else:
        form = UserLogin()

    return render(request, "apptelas/login.html", {"form": form})


def enviar_email_verificacao_view(request):
    return render(request, 'apptelas/enviar_email_verificacao.html')


def conta_ativada_view(request):
    return render(request, 'apptelas/conta_ativada.html')


@login_required(login_url='/login/')
def dashboard_view(request):
    return render(request, 'apptelas/dashboard.html')


disciplinas = [
    {
        'id': 1,
        'nome': 'Banco de Dados',
        'descricao': 'Descrição da disciplina de Banco de Dados',
    },
    {
        'id': 2,
        'nome': 'Programação Web',
        'descricao': 'Descrição da disciplina de Programação Web com foco em desenvolvimento fullstack.',
    },
    {
        'id': 3,
        'nome': 'Engenharia de Software',
        'descricao': 'Aborda o ciclo de vida do desenvolvimento de software e boas práticas de projeto.',
    }
]
calendarios = [
    {
        'id': 1,
        'nome': 'Calendário Banco de Dados',
        'disciplina': 'Banco de Dados'
    },
    {
        'id': 2,
        'nome': 'Calendário Programação Web',
        'disciplina': 'Programação Web'
    },
    {
        'id': 3,
        'nome': 'Calendário Engenharia de Software',
        'disciplina': 'Engenharia de Software'
    }
]
@login_required(login_url='/login/')
def disciplinas_view(request):
    return render(request, 'apptelas/disciplinas.html', {'disciplinas': disciplinas})


@login_required(login_url='/login/')
def disciplina_detail_view(request, id):
    return render(request, 'apptelas/disciplina_detail.html', {'disciplina': disciplinas[id-1]})


@login_required(login_url='/login/')
def configuracoes_view(request):
    return render(request, 'apptelas/configuracoes.html')


@login_required(login_url='/login/')
def calendarios_view(request):
    return render(request, 'apptelas/calendarios.html', {'calendarios': calendarios})


@login_required(login_url='/login/')
def calendario_detail_view(request, id):
    return render(request, 'apptelas/calendario_detail.html', {'calendario': calendarios[id-1]})


@login_required(login_url='/login/')
def avaliacoes_view(request):
    return render(request, 'apptelas/avaliacoes.html')


@login_required(login_url='/login/')
def tarefas_view(request):
    return render(request, 'apptelas/tarefas.html')

