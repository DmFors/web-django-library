from . import views
from django.urls import path

urlpatterns = [
    path('', views.library_home, name='library_home'),
    path('add_book', views.add_book, name='add_book'),
]