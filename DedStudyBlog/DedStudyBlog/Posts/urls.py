from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = 'Posts'

urlpatterns = [
    path('', index, name='index')
]