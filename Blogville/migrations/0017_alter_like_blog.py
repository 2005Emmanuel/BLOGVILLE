# Generated by Django 4.1.5 on 2023-02-04 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blogville', '0016_alter_like_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogville.blogpost'),
        ),
    ]
