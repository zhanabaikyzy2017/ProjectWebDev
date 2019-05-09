from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Book,Author,Publisher,UserProfile,Category,Quotation
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = UserProfile
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    added_by = UserProfileSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ('id','author','publisher','category','year','added_by','page_amount')

class QuotationSerializer(serializers.ModelSerializer):
    user = UserSerializer
    book = BookSerializer

    class Meta:
        model = Quotation
        fields = '__all__'

