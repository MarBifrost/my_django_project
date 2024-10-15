from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Sum, F, Max, Min, Avg

from .models import Product, Category


def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('store:store')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'store/login.html')


def logout_views(request):
    logout(request)
    return redirect('store:login')


def category(request):
    categories = Category.objects.exclude(parent_id=None)
    for category in categories:
        category.product_count = Product.objects.filter(category=category).count()
    return render(request, 'store/index.html', {'categories': categories})


def product_views_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    total_price = products.aggregate(total_price=Sum(F('quantity') * F('price')))
    the_most_price = products.aggregate(max=Max('price'))
    the_min_price = products.aggregate(min=Min('price'))
    the_avg_price = products.aggregate(avg=Avg('price'))
    context = {
        'products': products,
        'category': category,
        'total_price': total_price['total_price'],
        'the_most_price': the_most_price['max'],
        'the_min_price': the_min_price['min'],
        'the_avg_price': the_avg_price['avg'],
    }
    return render(request, 'store/products_list.html', context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'store/prod_details.html', {'product': product})
