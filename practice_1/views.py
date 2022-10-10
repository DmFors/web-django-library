from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group

from .forms import MyUserCreationForm, MyAuthenticationForm


def redirect_library(request):
    return redirect('book-list', permanent=True)


class RegisterUser(CreateView):
    form_class = MyUserCreationForm
    template_name = 'register.html'
    success_url = 'book-list'

    def form_valid(self, form):
        user = form.save()
        user.groups.add(Group.objects.get(name='users'))
        login(self.request, user)
        return redirect(self.success_url)


class LoginUser(LoginView):
    form_class = MyAuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('book-list')


def logout_user(request):
    logout(request)
    return redirect('login')
