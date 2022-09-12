from django.http import HttpResponse


def index(request):
    html = "Hello world"
    return HttpResponse(html)
