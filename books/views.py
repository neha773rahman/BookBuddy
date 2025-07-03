from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book, Progress, Review
from .serializers import BookSerializer, ProgressSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer


# Book create
class BookListCreateView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#book detail

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


# Progress Views
class ProgressView(generics.RetrieveUpdateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

# Review Views
class ReviewView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

