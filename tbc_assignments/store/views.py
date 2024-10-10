from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .models import Product, Category
from django.http import JsonResponse
from django.core.serializers import serialize




def store(request):
    return render(request, 'store/index.html')


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

def return_products(request):
    products = Product.objects.prefetch_related('category').all()
    res = []
    for product in products:
        res.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'category': product.category.name,
            'photo': product.photo.url if product.photo else None
        })
    return JsonResponse(list(res), safe=False)


def return_categories(request):
    res = Category.objects.all().values('name')
    return JsonResponse(list(res), safe=False)



