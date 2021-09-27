from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .cart import Cart
from .models import Product
from .forms import ProductCreationForm, CartAddProductForm

from django.contrib.auth.models import User


def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


@login_required
def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_details.html', {'product': product,
                                                         'cart_product_form': cart_product_form})
    # product = Product.objects.get(slug=slug)
    # return render(request, 'shop/product_details.html', {'product': product})


def search_result(request):
    search_value = request.GET.get('search')
    search_result = Product.objects.filter(model__icontains=search_value)
    return render(request, 'shop/search_result.html', {'search_result': search_result})


def product_create(request):
    if request.method == "GET":
        if request.user.is_superuser:
            return render(request, 'shop/product_create.html', {'form': ProductCreationForm})
        else:
            return render(request, 'user/no_permission.html')

    else:
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            return render(request, 'shop/product_create.html',
                          {'form': ProductCreationForm,
                           'error': 'Введены некоректные данные или такой товар уже существует'})


def loginUser(request):
    if request.method == "GET":
        return render(request, 'user/loginUser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user/loginUser.html',
                          {'form': AuthenticationForm, 'error':
                              "Неверно введен логин и/или пароль"})
        else:
            login(request, user)
            return redirect(request.GET.get('next')) if request.GET.get('next') else redirect('index')


def signupUser(request):
    if request.method == 'GET':
        return render(request, 'user/signupUser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(request.GET.get('next')) if request.GET.get('next') else redirect('index')
            except IntegrityError:
                return render(request, 'user/signupUser.html', {'form': UserCreationForm, 'error':
                    "Данное имя уже используется. Пожалуйста, попробуйте другое"})
        else:
            return render(request, 'user/signupUser.html', {'form': UserCreationForm, 'error':
                "Пароли не совпадают"})


@login_required
def logoutUser(request):
    logout(request)
    return redirect('index')


# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
