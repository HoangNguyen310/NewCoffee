from django.shortcuts import render
from django.views import View
from product.models import Category, Product


class ProductController(View):
    def product(request, category_id):
        category = Category.objects.filter(active=1)
        cate = Category.objects.get(id=category_id)
        product = cate.product_set.all()
        return render(request, 'product.html', {
            'product': product,
            'category': category
        })

    def detail(request, product_id):
        category = Category.objects.filter(active=1)
        detail = Product.objects.get(id=product_id)
        return render(request, 'detail.html', {
            'detail': detail,
            'category': category
        })
