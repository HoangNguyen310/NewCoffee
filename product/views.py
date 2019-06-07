from django.shortcuts import render, get_object_or_404
from django.views import View
from product.models import Category, Product


class ProductController(View):
    def product(request, cate_slug):
        category = Category.objects.filter(active=1)

        quantity = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                quantity += int(value['quantity'])
        except:
            pass

        cate = get_object_or_404(Category, slug=cate_slug)
        product = cate.product_set.all()
        return render(request, 'product.html', {
            'category': category,
            'cart_quantity': quantity,
            'cate': cate,
            'product': product
        })

    def detail(request, product_slug):
        category = Category.objects.filter(active=1)

        quantity = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                quantity += int(value['quantity'])
        except:
            pass

        detail = get_object_or_404(Product, slug=product_slug)
        cate = Category.objects.get(id=detail.category_id)
        product = Product.objects.all()
        return render(request, 'detail.html', {
            'detail': detail,
            'category': category,
            'cart_quantity': quantity,
            'product': product,
            'cate': cate
        })
