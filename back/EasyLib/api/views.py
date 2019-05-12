
from .models import Book,Category,Publisher,Review,Author
from .serializers import BookSerializer,CategorySerializer,PublisherSerializer,ReviewSerializer,AuthorSerializer
from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import UserManager


class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    #permission_classes = (IsAuthenticated,)

class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    #permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
class PublisherList(generics.ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    #permission_classes = (IsAuthenticated,)
class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    #permission_classes = (IsAuthenticated,)

class ReviewListOfOneBook(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    #permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        try:
            book = Book.objects.get(id=self.kwargs.get('pk'))
        except Review.DoesNotExist:
            raise Http404

        queryset = book.reviews.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()



