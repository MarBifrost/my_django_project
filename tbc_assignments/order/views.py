from django.shortcuts import render, redirect
from .models import Order


def order(request):
    return render(request, 'order/index.html')


def payment_success(request):
    if request.method == 'POST':
        product = request.POST['product']
        name = request.POST['name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        shipping_address = request.POST['shipping_address']

        order = Order(
            product=product,
            name=name,
            last_name=last_name,
            phone=phone,
            shipping_address=shipping_address,
        )
        order.save()
        return render(request, 'order/payment_success.html')
    return render(request, 'order/payment_success.html')
