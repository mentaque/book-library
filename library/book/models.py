from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    date_of_death = models.IntegerField()
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview_image = models.ImageField(upload_to="static/images")
    text = models.TextField()
    creation_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="books")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

