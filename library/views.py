from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from . import models
from . import forms


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

    book_form = forms.BookForm
    data = {
        'form': book_form,
        'error': error,
    }
    return render(request, 'library/change_book.html', data)


class BookUpdateView(UpdateView):
    model = models.Book
    fields = ['name', 'author', 'cost', 'publish_year']
    template_name = 'library/change_book.html'
