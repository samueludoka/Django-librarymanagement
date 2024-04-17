from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .models import Authors
from .serializers import BookSerializer, AuthorsSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'GET':
        book = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def author_list(request):
    if request.method == 'GET':
        author = Authors.objects.all()
        serializer = AuthorsSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = AuthorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail(request, pk, segno=None):
    author = get_object_or_404(Authors, id=pk)
    if request.method == 'GET':
        author = get_object_or_404(Authors, id=pk)
        serializer = AuthorsSerializer(author)
        author_qrcode = segno.make_qrl("welcome to Django")
        author_qrcode.save("welcome.png")
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = AuthorsSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)











