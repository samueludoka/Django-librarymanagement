from django.template.defaultfilters import pprint
from django.urls import path, include
from rest_framework_nested import routers

from . import views
from rest_framework.routers import SimpleRouter
from rest_framework.routers import DefaultRouter

# router = SimpleRouter()
# router = DefaultRouter

router = routers.DefaultRouter()

router.register("books", views.BookViewSet, "books"),
router.register("author", views.AuthorsViewSet, "author"),

review_router = routers.NestedDefaultRouter(router, "books", lookup='book')
review_router.register("reviews", views.ReviewViewSet, 'review')

book_image_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
book_image_router.register('book_image', views.BookImageViewSet, 'book_image')
urlpatterns = router.urls

urlpatterns = [
    # path('books/', views.BookList.as_view(), name='books'),
    # path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('', include(router.urls)),
    path('', include(review_router.urls)),
    path('', include(book_image_router.urls)),
    # path('author/', views.AuthorsList.as_view(), name="author"),
    # path('author/<int:pk>/', views.AuthorsDetails.as_view(), name='author_detail'),

]
