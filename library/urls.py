from django.urls import path
from .views import BookCreateView, BookListView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('create', BookCreateView.as_view(), name='create-book'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='update-book'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='delete-book'),
]
