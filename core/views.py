from django.shortcuts import render
from django.views import View
from product.models import Category, Product


class HomeController(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()
        return render(request, 'index.html', {
            'category': category,
            'product': product
        })


class LoginController(View):
    def get(self, request):
        return render(request, 'login.html')


class ContactController(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'contact.html', {
            'category': category
        })


class AboutController(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'about.html', {
            'category': category
        })