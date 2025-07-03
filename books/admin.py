from django.contrib import admin

# Register your models here.
from .models import Book, Progress, Review

admin.site.register(Book)
admin.site.register(Progress)
admin.site.register(Review)
