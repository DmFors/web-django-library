from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from . import forms


class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name_suffix = '_create_form'


class BookListView(ListView):
    model = models.Book
    paginate_by = 2

    def get_paginate_by(self, queryset):
        paginate = self.request.GET.get("paginate_by", self.paginate_by)
        return paginate


class BookUpdateView(UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name_suffix = '_update_form'


class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('library_home')
