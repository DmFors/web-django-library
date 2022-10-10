from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import MyUserCreationForm


def redirect_library(request):
    return redirect('book-list', permanent=True)


class RegisterUser(CreateView):
    form_class = MyUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('book-list')
