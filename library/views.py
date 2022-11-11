from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models
from . import forms
from cart.forms import CartAddBookForm


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name_suffix = '_create_form'

    login_url = 'login'

    def has_permission(self):
        try:
            role = self.request.session['role']
        except KeyError:
            role = 0
        return role > 0


class BookListView(ListView):
    model = models.Book
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        cart_add_book_form = CartAddBookForm()
        context['cart_add_book_form'] = cart_add_book_form
        return context

    def get_paginate_by(self, queryset):
        paginate = self.request.GET.get("paginate_by", self.paginate_by)
        return paginate

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = self.model.objects.all()
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name_suffix = '_update_form'

    login_url = 'login'

    def has_permission(self):
        try:
            role = self.request.session['role']
        except KeyError:
            role = 0
        return role == 2


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = models.Book
    success_url = reverse_lazy('book_list')

    login_url = 'login'

    def has_permission(self):
        try:
            role = self.request.session['role']
        except KeyError:
            role = 0
        return role == 2
