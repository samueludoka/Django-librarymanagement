from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template.context_processors import request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book, Review, BookImage
from .models import Authors
import segno
from .pagination import DefaultPagination
from .serializers import BookSerializer, AuthorsSerializer, ReviewSerializer, BookImageSerializer


# Create your views here.
# class BookList(APIView):
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def get(self, request):
#         book = Book.objects.all()
#         serializer = BookSerializer(book, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)

# the above commented method is rewritten below:

class BookViewSet(ModelViewSet):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ["title", "author"]


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookDetail(APIView):
#
#     def DELETE(self, request, pk):
#         book = get_object_or_404(Book, id=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     def GET(request, pk):
#         book = get_object_or_404(Book, id=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def PUT(request, pk):
#         book = get_object_or_404(Book, id=pk)
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


# the above commented method is rewritten below:
class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class AuthorsList(APIView):
#     def POST(self, request):
#         author = Authors.objects.all()
#         serializer = AuthorsSerializer(author, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def GET(self, request):
#         serializer = AuthorsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorsViewSet(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name']
    Ordering_fields = ['first_name']


# class AuthorsList(ModelViewSet):
#     queryset = Authors.objects.all()
#     serializer_class = AuthorsSerializer
#

# class AuthorsDetails(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Authors, pk=pk)
#         serializer = AuthorsSerializer(author)
#         author_data = segno.make_qr("welcome to Django")
#         author_data.save("welcome.png")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Authors, pk=pk)
#         serializer = AuthorsSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Authors, pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorsDetails(ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Authors, id=pk)
#     if request.method == 'GET':
#         serializer = AuthorsSerializer(author)
#         author_data = segno.make_qr("welcome to Django")
#         author_data.save("welcome.png")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorsSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class Review(ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_pk': self.kwargs['book_pk']}


class BookImageViewSet(ModelViewSet):
    serializer_class = BookImageSerializer

    def get_queryset(self):
        return BookImage.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_pk': self.kwargs['book_pk']}
