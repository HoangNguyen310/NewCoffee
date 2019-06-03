from django.shortcuts import render
from django.views import View
from product.models import Category
from cart.models import *


class CartController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)
        item = CartItem.objects.all()
        total = 0
        for i in item:
            total = total + i.price
        all = total + 30000
        return render(request, 'cart.html', {
            'category': category,
            'cart_item': item,
            'total_price': total,
            'all': all
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
