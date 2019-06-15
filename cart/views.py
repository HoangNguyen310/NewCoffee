from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views import View
from product.models import Category
from cart.models import *

cart = {}


class CartController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)
        cart = request.session['cart']

        quantity = 0
        for key, value in cart.items():
            quantity += int(value['quantity'])

        total = 0
        if len(cart) > 0:
            for key, value in cart.items():
                if int(value['sale']) > 0:
                    total += int(value['sale']) * int(value['quantity'])
                else:
                    total += int(value['price']) * int(value['quantity'])
            return render(request, 'cart.html', {
                'category': category,
                'cart_quantity': quantity,
                'total': total,
            })
        else:
            return render(request, 'empty_cart.html', {
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

        return render(request, 'cart.html')

    def update_cart(request):
        if request.is_ajax():
            id = request.POST['id']
            num = request.POST['quantity']
            product = Product.objects.get(id=id)
            if id in cart.keys():
                item = {
                    'name': product.title,
                    'price': product.price,
                    'sale': product.sale,
                    'quantity': num
                }

        cart[id] = item
        request.session['cart'] = cart

        return render(request, 'cart.html')

    def remove_cart(request):
        if request.is_ajax():
            id = request.POST['id']
            if id in cart.keys():
                del cart[id]

        request.session['cart'] = cart

        return render(request, 'cart.html')


class CheckoutController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)
        return render(request, 'checkout.html', {
            'category': category
        })


class PaymentController(View):
    def get(self, request):
        category = Category.objects.filter(active=1)

        quantity = 0
        total = 0
        for key, value in cart.items():
            quantity += int(value['quantity'])
            if int(value['sale']) > 0:
                total += int(value['sale']) * int(value['quantity'])
            else:
                total += int(value['price']) * int(value['quantity'])

        return render(request, 'payment.html', {
            'category': category,
            'cart_quantity': quantity,
            'total': total
        })

    def post(request):
        name = request.POST['Name']
        address = request.POST['Address']
        email = request.POST['Email']

        lst = []

        total = 0
        for key, value in cart.items():
            item = CartItem()
            item.title = value['name']
            item.product_id = int(key)
            item.quantity = value['quantity']
            if int(value['sale']) > 0:

                item.price = int(value['sale'])
                total += int(value['sale']) * int(value['quantity'])
            else:
                item.price = int(value['price'])
                total += int(value['price']) * int(value['quantity'])
            item.save()
            lst.append(value['name'] + ' - ' + str(value['quantity']))

        c = Cart()
        c.user = name
        c.total = total
        c.save()

        message = 'Xin chào {0}, đơn hàng của bạn đã được đặt thành công.\nCác món bạn đã đặt là {1}.\nTổng giá trị đơn hàng là {2} vnđ (chưa bao gồm phí vận chuyển).\nĐịa chỉ giao hàng: {3}.\nCảm ơn quí khách đã sử dụng dịch vụ.'.format(name, lst, total, address)

        send_mail(
            'New Coffee',
            message,
            'newcoffee138hadac@gmail.com',
            [email]
        )

        cart.clear()
        request.session['cart'] = cart

        return redirect('home:index')

