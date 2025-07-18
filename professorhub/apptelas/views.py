from django.shortcuts import render, redirect
from .forms import UserRegister#, UserLogin
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, 'apptelas/index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        print('erros...')
        print(form.errors)
        return render(request, 'apptelas/register.html', {
            'form': form,
        })
    
    # senha: rsA/47y£kI-6
    form = UserRegister()
    return render(request, 'apptelas/register.html', {'form': form})


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


@login_required(login_url='/login/')
def planos_aula_view(request):
    return render(request, 'apptelas/planos-de-aula.html')

