from django.shortcuts import render
from django.views import View
from product.models import Category
from cart.models import *


class CartController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)
        return render(request, 'cart.html', {
            'category': category
        })

    def cart(self, request):
        item = CartItem.objects.all()
        return render(request, 'cart.html', {
            'cart_item': item
        })


class CheckoutController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)
        return render(request, 'checkout.html', {
            'category': category
        })


class PaymentController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)
        return render(request, 'payment.html', {
            'category': category
        })
