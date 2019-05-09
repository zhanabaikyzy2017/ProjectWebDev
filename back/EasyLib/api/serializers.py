from rest_framework import serializers
from django.contrib.auth.models import User
<<<<<<< HEAD
from api.models import Book,Author,Publisher,UserProfile,Category,Review
=======
from ..api.models import Book,Author,Publisher,UserProfile,Category,Quotation
>>>>>>> 0faff589a477b1fe35164cd60c6f2f26620c23ea
class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
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
        fields = ('mobile','website','join_date','book')


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = AuthorSerializer
    publisher = PublisherSerializer
    category = CategorySerializer


    class Meta:
        model = Book
        fields = ('id','title','author','publisher','category','year','page_amount')

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer
    book = BookSerializer

    class Meta:
        model = Review
        fields = '__all__'

