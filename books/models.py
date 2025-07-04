from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here

class Book(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Reading'),
        ('completed', 'Completed'),
        ('wishlist', 'Wishlist'),
    ]

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    genre = models.CharField(max_length=100)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')

    total_pages = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Progress(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    percent_completed = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} - {self.percent_completed}% on {self.updated_at}"


class Review(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='review')
    notes = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)  # 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title}"
    

