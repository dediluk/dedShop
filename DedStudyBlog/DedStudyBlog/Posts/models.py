from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify
import datetime


class Post(models.Model):
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст поста')
    draft = models.BooleanField('Черновик')
    date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return self.title

    def slug(self):
        return slugify(self.title)

