from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import User

from django.views.generic import CreateView, FormView
from django.contrib.auth import logout

from .forms import MyUserCreationForm, MyAuthenticationForm


def redirect_library(request):
    return redirect('book-list', permanent=True)


class RegisterUser(CreateView):
    form_class = MyUserCreationForm
    template_name = 'main/register.html'
    success_url = 'book-list'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class LoginUser(FormView):
    form_class = MyAuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse('book-list')

    def form_valid(self, form):
        form_data = form.cleaned_data
        try:
            user = User.objects.get(username=form_data['username'])
        except User.DoesNotExist:
            form.add_error(None, 'Неверный логин!')
            return super().form_invalid(form)

        if user.check_password(form_data['password']):
            self.request.session['username'] = user.username
            self.request.session['role'] = user.role
            return super().form_valid(form)
        else:
            form.add_error(None, 'Неверный пароль!')
            return super().form_invalid(form)


def logout_user(request):
    logout(request)
    return redirect('login')
