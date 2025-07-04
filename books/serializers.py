from rest_framework import serializers
from .models import Book, Progress, Review


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'book', 'percent_completed', 'updated_at']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'rating', 'notes', 'created_at']

    def validate(self, data):
        if not data.get('rating') and not data.get('notes'):
            raise serializers.ValidationError("Either rating or notes must be provided.")
        return data

class BookSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)  # nested review

    class Meta:
        model = Book
        fields = '__all__'

class BookDetailSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'status', 'total_pages', 'review']

class ProgressHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['updated_at', 'percent_completed']

