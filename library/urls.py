from django.urls import path
from .views import BookCreateView, BookListView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('create', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),
]
