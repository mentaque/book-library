# Generated by Django 4.1.7 on 2023-03-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_author_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='popular_book',
            field=models.BooleanField(default=False),
        ),
    ]
