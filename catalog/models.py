from uuid import uuid4
# from userApp.model import LibraryUser
from django.conf import settings
from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey('Authors', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def list_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:2])


class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Language(models.Model):
    name = models.CharField(max_length=255)


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('A', 'Available'),
        ('U', 'Unavailable'),
    ]
    unique_id = models.UUIDField(default=uuid4, primary_key=True)
    due_back = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
