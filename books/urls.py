from django.urls import path
from .views import BookListCreateView, BookDetailView, ProgressView, ReviewView,RegisterView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('progress/<int:pk>/', ProgressView.as_view(), name='book-progress'),
    path('review/<int:pk>/', ReviewView.as_view(), name='book-review'),
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

]
