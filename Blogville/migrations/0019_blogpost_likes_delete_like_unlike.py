# Generated by Django 4.1.5 on 2023-02-05 11:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blogville', '0018_like_unlike_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Like_unlike',
        ),
    ]
