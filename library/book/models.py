from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import date


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    short_description = models.TextField(default='asd')
    biography = models.TextField(default='asd')
    date_of_birth = models.DateField(default=date.today)
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
    century = models.IntegerField(default=20)
    creation_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    popular_book = models.BooleanField(default=False)

    def average_rating(self):
        ratings = self.bookrating_set.all()
        if ratings.exists():
            return sum(r.rating for r in ratings) / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.title


class User(AbstractUser):
    pass


class UserBookRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    in_bookmarks = models.BooleanField(default=False)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)




