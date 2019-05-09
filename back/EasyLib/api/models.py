from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()


class Publisher(models.Model):
    name = models.CharField(max_length=200)


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    website= models.CharField(max_length=50,null=True)
    join_date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=200,default='')


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    author = models.ForeignKey(Author ,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    page_amount = models.IntegerField()
    added_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

class Quotation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    quotation = models.CharField(max_length=600)
    creation_date = models.DateTimeField(auto_now_add=True)


