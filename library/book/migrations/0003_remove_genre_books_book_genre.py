# Generated by Django 4.1.7 on 2023-03-14 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_author_books_book_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.genre'),
        ),
    ]