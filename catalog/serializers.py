from rest_framework import serializers

from catalog.models import Book, Authors


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['first_name', 'last_name', 'date_of_birth']
