from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book, Progress, Review
from .serializers import BookSerializer, ProgressSerializer, ReviewSerializer

# Book Views
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Progress Views
class ProgressView(generics.RetrieveUpdateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

# Review Views
class ReviewView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
