# Generated by Django 4.1.4 on 2022-12-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movieorder_movie_movie_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieorder',
            name='buyed_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
