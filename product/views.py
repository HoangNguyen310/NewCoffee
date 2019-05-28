from django.shortcuts import render
from django.views import View
from product.models import Category, Product


class ProductController(View):
    def product(request, category_id):
        model = Category.objects.get(id=category_id)
        category = Category.objects.all()
        return render(request, 'product.html', {
            'product': model,
            'category': category
        })

    def detail(request, product_id):
        category = Category.objects.all()
        model = Product.objects.get(id=product_id)
        return render(request, 'detail.html', {
            'detail': model,
            'category': category
        })
