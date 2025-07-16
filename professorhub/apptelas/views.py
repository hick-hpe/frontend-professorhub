from django.shortcuts import render, redirect
from .forms import UserRegister#, UserLogin
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/login/')
def teste_view(request):
    return render(request, 'apptelas/teste.html')


