from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    date_of_death = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True)
    photo = models.ImageField(upload_to="static/images")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_page', kwargs={'author_slug': self.slug})


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview_image = models.ImageField(upload_to="static/images")
    text = models.TextField()
    creation_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title


