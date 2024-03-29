# Generated by Django 4.1.7 on 2023-03-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_alter_news_description_alter_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='banner',
            field=models.ImageField(null=True, upload_to='news/banners/', verbose_name='Банер'),
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='news/images/', verbose_name='Зображення'),
        ),
    ]
