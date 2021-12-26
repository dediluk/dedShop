from django.urls import path
from .views import *

# Todo Корзина
# Todo ? Войти как тестовый покупатель
# Todo Возможно, изменить форму регистрации на стандартную Django
# Todo Изменение пароля, логина
# Todo Сброс пароля
# Todo Редактирование товара


urlpatterns = [
    path('', index, name='index'),
    path('search/', search_result, name='search_result'),
    path('product/<slug:slug>', product_details, name='product_details'),
    path('product/create/', product_create, name='product_create'),

    # accounts
    path('signup/', signupUser, name='signupUser'),
    path('accounts/login/', loginUser, name='loginUser'),
    path('accounts/logout/', logoutUser, name='logoutUser'),

    path('cart/', cart_detail, name='cart_detail'),
    path('cart/add/<str:product_id>', cart_add, name='cart_add'),
    path('cart/remove/<str:product_id>', cart_remove, name='cart_remove'),
    path('cart/order_create/', order_create, name='order_create'),

]
