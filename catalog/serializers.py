from rest_framework import serializers

from catalog.models import Book, Authors


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        queryset=Authors.objects.all(),
        view_name='author_detail'
    )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']
