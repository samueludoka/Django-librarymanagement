from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),

    path('author/', views.author_list, name="author"),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),

]
