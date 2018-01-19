import datetime
from django.db import models
from django.utils import timezone

# Table Book
class Book (models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date_publish = models.DateTimeField(null=True)
    number_of_page = models.CharField(max_length=10, blank=True, null=True)
    type_of_book = models.CharField(max_length=150, blank=True, null=True)