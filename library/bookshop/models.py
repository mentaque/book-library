from django.db import models

from book.models import Author, User


class Producer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class BookProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to="static/images/for-shop")
    length = models.IntegerField()
    width = models.IntegerField()
    weight = models.IntegerField()
    county_producer = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True)


class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(BookProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
