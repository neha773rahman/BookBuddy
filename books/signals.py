from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, Progress, Review

@receiver(post_save, sender=Book)
def create_progress_and_review(sender, instance, created, **kwargs):
    if created:
        Progress.objects.create(book=instance)
        Review.objects.create(book=instance)
