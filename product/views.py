from django.shortcuts import render, get_object_or_404
from django.views import View
from product.models import Category, Product
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger


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
        detail = get_object_or_404(Product, slug=product_slug)
        cate = Category.objects.get(id=detail.category_id)

        quantity = 0
        try:
            cart = request.session['cart']
            for key, value in cart.items():
                quantity += int(value['quantity'])
        except:
            pass

        product = Product.objects.all()

        return render(request, 'detail.html', {
            'detail': detail,
            'category': category,
            'cart_quantity': quantity,
            'product': product,
            'cate': cate
        })

    def all(request):
        category = Category.objects.filter(active=1)

        product_list = Product.objects.all()
        paginator = Paginator(product_list, 12)
        page = request.GET.get('page', 1)
        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        return render(request, 'all.html', {
            'category': category,
            'product': product
        })

