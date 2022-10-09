from django.shortcuts import redirect


def redirect_library(request):
    return redirect('book-list', permanent=True)
