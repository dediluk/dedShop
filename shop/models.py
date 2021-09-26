import pytils
from django.db import models
from django.contrib import admin
from django.urls import reverse
from autoslug import AutoSlugField


class Manufacturer(models.Model):
    title = models.CharField(verbose_name='Производитель', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    # Todo Изображение товара
    model = models.CharField(verbose_name='Модель товара', max_length=50)
    description = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Цена')
    availability = models.BooleanField(verbose_name='Есть в наличии')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.DO_NOTHING)
    # slug = models.SlugField(null=True)
    slug = AutoSlugField(populate_from='model')

    def __str__(self):
        return str(self.manufacturer) + " " + self.model

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'manufacturer', 'availability', 'price')
