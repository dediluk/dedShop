from django.shortcuts import render
from .models import Post


def index(request):
    posts = list(Post.objects.all())[::-1] #Новые посты идут первыми
    return render(request, 'posts/index.html', {"posts": posts})
