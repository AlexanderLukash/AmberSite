# Generated by Django 4.1.7 on 2023-03-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_remove_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='news/images/', verbose_name='Зображення'),
        ),
    ]
