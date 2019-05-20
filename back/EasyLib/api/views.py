from .models import Book,Category,Review,UserProfile,Author
from .serializers import BookSerializer,CategorySerializer,ReviewSerializer,UserProfileSerializer,AuthorSerializer
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
    # permission_classes = (IsAuthenticated,)

class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ReviewList(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewListOfOneBook(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        try:
            book = Book.objects.get(id=self.kwargs.get('pk'))
        except Review.DoesNotExist:
            raise Http404
        queryset = book.books.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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

class BookCreate(generics.CreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        try:
            category = Category.objects.get(id=self.kwargs.get('pk'))
        except Review.DoesNotExist:
            raise Http404
        queryset = category.books.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(category=Category.objects.get(id=self.kwargs.get('pk')),
                        author=Author.objects.get(id = self.kwargs.get('pk2')))

class AuthorBooks(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        try:
            author = Author.objects.get(id=self.kwargs.get('pk'))
        except Author.DoesNotExist:
            raise Http404
        queryset = author.books.all()
        return queryset


class UserProfileDetail(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        try:
            userProf = UserProfile.objects.filter(user=self.request.user)
        except Review.DoesNotExist:
            raise Http404
        return userProf

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UserProfBooks(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        try:
            userPtof = UserProfile.objects.get(id = self.kwargs.get('pk'))
        except UserProfile.DoesNotExist:
            raise Http404
        queryset = userPtof.book.all()
        return queryset
