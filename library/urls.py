from django.urls import path
from .views import BookCreateView, BookListView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('create', BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
]
