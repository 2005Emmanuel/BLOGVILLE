# Generated by Django 4.1.5 on 2023-02-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogville', '0009_alter_blogpost_image_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='kindpng_4212275.png', null=True, upload_to='profile_pictures'),
        ),
    ]
