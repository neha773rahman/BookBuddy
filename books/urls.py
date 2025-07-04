from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    ProgressView,
    ReviewView,
    ProgressHistoryView,
    ReviewCreateView,
    ProgressCreateView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('progress/<int:pk>/', ProgressView.as_view(), name='book-progress'),
    path('books/<int:book_id>/progress/', ProgressCreateView.as_view(), name='add-progress'),
    path('progress/', ProgressCreateView.as_view()),

    path('reviews/', ReviewCreateView.as_view()),    
    path('review/<int:pk>/', ReviewView.as_view(), name='book-review'),
    path('books/<int:book_id>/progress-history/', ProgressHistoryView.as_view(), name='progress-history'),
]



