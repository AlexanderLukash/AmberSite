# Generated by Django 4.1.7 on 2023-03-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/images/', verbose_name='Зображення'),
        ),
    ]
