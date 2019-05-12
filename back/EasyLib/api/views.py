

from .models import Book,Category,Publisher,Review,Author
from .serializers import BookSerializer,CategorySerializer,PublisherSerializer,ReviewSerializer,AuthorSerializer
from rest_framework.decorators import api_view

from .models import Book
from .serializers import BookSerializer

from .models import Book,Category,Publisher,Review,UserProfile,Author
from .serializers import BookSerializer,CategorySerializer,PublisherSerializer,ReviewSerializer,UserProfileSerializer
from rest_framework.decorators import api_view

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
#
# @api_view(['GET'])
# def review_of_book(request, pk):
#     try:
#         reviews = Review.objects.get(book=pk)
#     except reviews.DoesNotExist as e:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     serializer = ReviewSerializer(reviews, many=True)
#
#     return Response(serializer.data,status=status.HTTP_200_OK)
#

class ReviewListOfOneBook(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        try:
            book = Book.objects.get(id=self.kwargs.get('pk'))
        except Review.DoesNotExist:
            raise Http404
        queryset = book.books.all()
        return queryset


        queryset = book.reviews.all()
        return queryset

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)



class UserProfileList(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class CategoryBooks(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        try:
            category = Category.objects.get(id=self.kwargs.get('pk'))
        except Review.DoesNotExist:
            raise Http404
        queryset = category.books.all()
        return queryset

class AuthorBooks(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        try:
            author = Author.objects.get(id=self.kwargs.get('pk'))
        except Review.DoesNotExist:
            raise Http404
        queryset = author.books.all()
        return queryset