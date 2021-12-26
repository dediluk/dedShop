# import pytils
from django.db import models
from django.contrib import admin
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import Group, User


# class Shop(models.Model):
#     name_of_shop = models.CharField(max_length=200, default='Название магазина', unique=True)
#     username = models.CharField(max_length=200, default='Название магазина', unique=True)


class Manufacturer(models.Model):
    title = models.CharField(verbose_name='Производитель', max_length=50, default='Manufacturer')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"


class Category(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=30, default='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    # Todo Изображение товара
    model = models.CharField(verbose_name='Модель товара', max_length=50, default='model', unique=True)
    description = models.TextField(verbose_name='Описание товара', default='description')
    price = models.IntegerField(verbose_name='Цена', default=100)
    availability = models.BooleanField(verbose_name='Есть в наличии', default='1')
    categories = models.ManyToManyField(Category, verbose_name='Категории', default='description')
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.DO_NOTHING)
    slug = AutoSlugField(populate_from='model')

    def __str__(self):
        return str(self.manufacturer) + " " + self.model

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField()
    address = models.CharField(verbose_name='Адрес', max_length=250)
    postal_code = models.CharField(verbose_name='Индекс', max_length=20)
    city = models.CharField(verbose_name='Город', max_length=100)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачен', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', related_name='items', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, verbose_name='Товар', related_name='order_items', on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, verbose_name='Цена', decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
