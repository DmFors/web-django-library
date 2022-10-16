from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class MyUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите логин'
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите email'
    }))

    first_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше имя'
    }))

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name']


class MyAuthenticationForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите логин',
    }))

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль',
    }))
