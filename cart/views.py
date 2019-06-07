from django.shortcuts import render
from django.views import View
from product.models import Category
from cart.models import *

cart = {}


class CartController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)

        quantity = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                quantity += int(value['quantity'])
        except:
            pass

        total = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                if int(value['sale']) > 0:
                    total += int(value['sale'])*int(value['quantity'])
                else:
                    total += int(value['price'])*int(value['quantity'])
            return render(request, 'cart.html', {
                'category': category,
                'cart_quantity': quantity,
                'total': total,
            })
        except:
            return render(request, 'emptycart.html', {
                'category': category,
                'cart_quantity': quantity
            })

    def add_cart(request):
        if request.is_ajax():
            id = request.POST['id']
            num = request.POST['quantity']
            product = Product.objects.get(id=id)
            if id in cart.keys():
                item = {
                    'name': product.title,
                    'price': product.price,
                    'sale': product.sale,
                    'quantity': int(cart[id]['quantity']) + int(num)
                }
            else:
                item = {
                    'name': product.title,
                    'price': product.price,
                    'sale': product.sale,
                    'quantity': num
                }

        cart[id] = item
        request.session['cart'] = cart

        return render(request, 'addcart.html')

    def del_cart(request):
        pass

    def cart(request):
        category = Category.objects.filter(active=1)
        total = 0
        cart = request.session['cart']
        for key, value in cart:
            total += int(value['price'])*int(value['quantity'])
        return render(request, 'cart.html', {
            'category': category,
            'total': total
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
