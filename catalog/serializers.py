from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from catalog.models import Book, Authors, Review


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['book', 'name', 'message', 'date']

        def created(self, validated_data):
            book_id = self.context['book_pk']
            return Review.objects.create(book_id=book_id, **validated_data)

