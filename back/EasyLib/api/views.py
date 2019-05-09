<<<<<<< HEAD
from api.models import Book,Category,Publisher,Review
from api.serializers import BookSerializer,CategorySerializer,PublisherSerializer,ReviewSerializer
from rest_framework.decorators import api_view
=======
from ..api.models import Book
from ..api.serializers import BookSerializer

>>>>>>> 0faff589a477b1fe35164cd60c6f2f26620c23ea
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import UserManager


class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated,)

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




