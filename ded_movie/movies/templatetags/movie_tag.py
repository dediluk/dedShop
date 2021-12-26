from django import template
from movies.models import Category, Movie

register = template.Library()


@register.simple_tag() #Возвращаем в header queryset всех категорий для отображения
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movies.html') #Указываем, какой тэг рендерить при вызове данного темплейт тэга
#При вызове тэга в sidebar передаем количество фильмов
def get_last_movies(count=5):
    last_movies = Movie.objects.order_by('id')[:count]
    return {'last_movies': last_movies}
