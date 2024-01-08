from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pick/store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items}
    return render(request, 'pick/cart.html', context)




def checkout(request):
    context = {}
    return render(request, 'pick/checkout.html', context)