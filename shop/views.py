from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})


@login_required
def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'shop/product_details.html', {'product': product})


def search_result(request):
    search_value = request.GET.get('search')
    search_result = Product.objects.filter(model__icontains=search_value)
    return render(request, 'shop/search_result.html', {'search_result': search_result})


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
