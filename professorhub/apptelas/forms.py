from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserRegister(UserCreationForm):
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome de usuário"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Senha"})
    )
    password2 = forms.CharField(
        label="Confirme sua senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirme sua senha"})
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLogin(AuthenticationForm):
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome de usuário"})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Senha"})
    )