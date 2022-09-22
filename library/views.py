from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
from django.urls import reverse, reverse_lazy
from . import models
from . import forms

from django.forms.widgets import Select


def library_home(request):
    data = {'books': models.Book.objects.all().order_by('publish_year')}
    return render(request, 'library/home.html', data)


def add_book(request):
    error = ''
    if request.method == 'POST':
        book_form = forms.BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('library_home')
        else:
            error = 'Форма неправильно заполнена!'
    else:
        book_form = forms.BookForm

    data = {
        'form': book_form,
        'error': error,
    }
    return render(request, 'library/add_book.html', data)


class BookListView(ListView):
    model = models.Book
    paginate_by = 2
    template_name = 'library/home.html'

    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)

class PaginationChoice(Select):
    pass


class BookUpdateView(UpdateView):
    model = models.Book
    template_name = 'library/update_book.html'
    form_class = forms.BookForm


class BookDeleteView(DeleteView):
    model = models.Book
    template_name = 'library/delete_book.html'
    success_url = reverse_lazy('library_home')
