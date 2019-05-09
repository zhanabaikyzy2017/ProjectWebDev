from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Publisher'
        verbose_name_plural = 'Publishers'


class Category(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    page_amount = models.IntegerField()
    author = models.ForeignKey(Author ,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

class Quotation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    quotation = models.CharField(max_length=600)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quotation'
        verbose_name_plural = 'Quotations'


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=True)
    website= models.CharField(max_length=50,null=True)
    join_date = models.DateTimeField(auto_now_add=True)
    book = models.ManyToManyField(Book)
