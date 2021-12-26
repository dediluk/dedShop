# Generated by Django 3.2.7 on 2021-09-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210925_1709'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'Производитель', 'verbose_name_plural': 'Производители'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default='test', max_length=50, verbose_name='Модель товара'),
            preserve_default=False,
        ),
    ]
