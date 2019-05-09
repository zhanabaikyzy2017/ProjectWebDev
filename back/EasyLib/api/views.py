from api.models import Book
from api.serializers import BookSerializer

from rest_framework import generics

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


