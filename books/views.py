from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Book, Progress, Review
from .serializers import (
    BookSerializer,
    ProgressSerializer,
    ReviewSerializer,
    BookDetailSerializer,
    ProgressHistorySerializer
)

@method_decorator(csrf_exempt, name='dispatch')
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        print("DATA COMING TO BACKEND:", self.request.data)
        serializer.save()


# Book detail with nested progress and review
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = []


# Progress Views
class ProgressView(generics.RetrieveUpdateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class ProgressCreateView(generics.CreateAPIView):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

# Review Views
class ReviewView(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class ProgressHistoryView(APIView):
    def get(self, request, book_id):
        history = Progress.objects.filter(book_id=book_id).order_by('updated_at')
        serializer = ProgressHistorySerializer(history, many=True)
        return Response(serializer.data)