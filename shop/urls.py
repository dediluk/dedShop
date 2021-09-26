from django.urls import path
from .views import *


# Todo Создание товара на странице



urlpatterns = [
    path('', index, name='index'),
    path('search/', search_result, name='search_result'),
    path('product/<slug:slug>', product_details, name='product_details'),


    # accounts
    path('signup/', signupUser, name='signupUser'),
    path('accounts/login/', loginUser, name='loginUser'),
    path('accounts/logout/', logoutUser, name='logoutUser'),

]
