from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Book,Author,Publisher
class AuthorSerializer(serializers.ModelSerializer):
    pass
class PublisherSerializer(serializers.ModelSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = AuthorSerializer
    publisher = PublisherSerializer
    added_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

