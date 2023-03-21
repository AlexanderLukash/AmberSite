# Generated by Django 4.1.7 on 2023-03-21 06:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=335, verbose_name='Передмова')),
                ('text', models.TextField(verbose_name='Описання')),
                ('premiere', models.DateField(default=datetime.date.today, verbose_name='Дата публікації')),
                ('url', models.SlugField(default='Введіть унікальний аудентифікатор', max_length=255, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Чернетка')),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
            },
        ),
    ]
