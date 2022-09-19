from django.shortcuts import render
from . import models


def library_home(request):
    data = {'books': models.Book.objects.all().order_by('publish_date')}
    return render(request, 'library/home.html', data)


def add_book(request):

    return render(request, 'library/add_book.html')
