# Generated by Django 4.1.7 on 2023-03-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_author_url_book_url_genre_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='url',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='url',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]