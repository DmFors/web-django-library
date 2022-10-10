from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models
from . import forms


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name_suffix = '_create_form'

    login_url = 'login'

    def has_permission(self):
        return self.request.user.groups.filter(name__in=['users', 'admins']).exists()


class BookListView(ListView):
    model = models.Book
    paginate_by = 2

    def get_paginate_by(self, queryset):
        paginate = self.request.GET.get("paginate_by", self.paginate_by)
        return paginate


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name_suffix = '_update_form'

    login_url = 'login'

    def has_permission(self):
        return self.request.user.groups.filter(name='admins').exists()


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Book
    success_url = reverse_lazy('book-list')

    login_url = 'login'

    def has_permission(self):
        return self.request.user.groups.filter(name='admins').exists()
