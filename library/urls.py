from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookListView.as_view(), name='library_home'),
    path('add_book', views.add_book, name='add_book'),
    path('<int:pk>/update', views.BookUpdateView.as_view(), name='update-book'),
    path('<int:pk>/delete', views.BookDeleteView.as_view(), name='delete-book'),
]
