from django.shortcuts import render, redirect
from django.views import View
from product.models import Category, Product
from .models import Slider


class HomeController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)
        slide = Slider.objects.filter(active=1)
        product = Product.objects.filter(active=1)

        quantity = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                quantity += int(value['quantity'])
        except:
            pass

        return render(request, 'index.html', {
            'category': category,
            'slide': slide,
            'product': product,
            'cart_quantity': quantity
        })


class LoginController(View):
    def get(self, request):
        return render(request, 'login.html')


class ContactController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)

        quantity = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                quantity += int(value['quantity'])
        except:
            pass

        return render(request, 'contact.html', {
            'category': category,
            'cart_quantity': quantity
        })


class AboutController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)

        quantity = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                quantity += int(value['quantity'])
        except:
            pass

        return render(request, 'about.html', {
            'category': category,
            'cart_quantity': quantity
        })
