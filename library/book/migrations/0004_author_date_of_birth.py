# Generated by Django 4.1.7 on 2023-03-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_author_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='date_of_birth',
            field=models.IntegerField(null=True),
        ),
    ]