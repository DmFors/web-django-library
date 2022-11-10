from django.http import JsonResponse

from .models import User
from django.views.generic import CreateView, UpdateView, FormView
from .forms import MyUserCreationForm, MyUserUpdateForm, MyAuthenticationForm
from django.contrib.auth.hashers import make_password

from django.shortcuts import redirect
from django.urls import reverse


def redirect_library(request):
    return redirect('book_list', permanent=True)


class RegisterUser(CreateView):
    form_class = MyUserCreationForm
    template_name = 'main/register.html'
    success_url = 'book_list'

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.password = make_password(password)
        user.save()

        self.request.session['user_id'] = user.id
        self.request.session['username'] = user.username
        self.request.session['role'] = user.role
        return redirect(self.success_url)


def validate_username(request):
    username = request.GET.get('username', None)
    response = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)

# def validate_password(request):
#     password = request.GET.get('password', None)
#     responce = {
#         'is_correct_length': len(password)
#     }

class LoginUser(FormView):
    form_class = MyAuthenticationForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse('book_list')

    def form_valid(self, form):
        form_data = form.cleaned_data
        try:
            user = User.objects.get(username=form_data['username'])
        except User.DoesNotExist:
            form.add_error(None, 'Неверный логин!')
            return super().form_invalid(form)

        if user.check_password(form_data['password']):
            self.request.session['user_id'] = user.id
            self.request.session['username'] = user.username
            self.request.session['role'] = user.role
            return super().form_valid(form)
        else:
            form.add_error(None, 'Неверный пароль!')
            return super().form_invalid(form)


def logout_user(request):
    try:
        del request.session['user_id']
        del request.session['username']
        del request.session['role']
        del request.session['cart']
    except KeyError:
        pass
    return redirect('login')


class UserUpdateView(UpdateView):
    model = User
    form_class = MyUserUpdateForm
    template_name_suffix = '_update_form'
    success_url = 'book_list'

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.password = make_password(password)
        user.save()
        return redirect(self.success_url)
