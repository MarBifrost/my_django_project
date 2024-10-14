from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count


from .models import Product, Category
from django.http import JsonResponse







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
    categories =  Category.objects.exclude(parent_id=None)
    for category in categories:
        category.product_count=Product.objects.filter(category=category).count()
    return render(request, 'store/index.html', {'categories': categories})


def product_views_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'category': category
    }
    return render(request, 'store/products_list.html', context)


def full_details_of_products(request):
    product = Product.objects.all()
    return render(request, 'store/product_full_info.html', {'products': product})


# def category(request):
#     categories =  Category.objects.exclude(parent_id=None)
#     products_in_categories = Product.objects.filter(category__in=category).count()
#     context = {'categories': categories, 'product_count': products_in_categories}
#     return render(request, 'store/index.html', context)


# def id_products(request):
#     products = Product.objects.prefetch_related('category').all()
#     res = []
#     for product in products:
#         res.append({
#             'id': product.id,
#             'name': product.name,
#             'price': product.price,
#             'category': product.category.name,
#             'photo': product.photo.url if product.photo else None
#         })
#     return JsonResponse(list(res), safe=False)
#
#
# def return_categories(request):
#     res = Category.objects.all().values('id', 'name')
#     return JsonResponse(list(res), safe=False)



