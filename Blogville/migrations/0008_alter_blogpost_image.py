# Generated by Django 4.1.5 on 2023-02-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogville', '0007_alter_blogpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, default='media\\profile_pictures\\kindpng_4212275.png', null=True, upload_to='profile_pictures'),
        ),
    ]
