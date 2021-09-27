# Generated by Django 3.2.7 on 2021-09-27 11:42

import autoslug.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_auto_20210927_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shops',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Магазины'),
        ),
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default='1', verbose_name='Есть в наличии'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(default='model', max_length=50, unique=True, verbose_name='Модель товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=100, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='model'),
        ),
    ]
