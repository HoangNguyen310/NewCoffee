from django.contrib import admin
from product.models import Category, Product
from cart.models import Cart, CartItem
from order.models import Order
from user.models import CustomerUser
from .models import Slider


class Filter(admin.ModelAdmin):
    list_filter = ['create_at']


class Search(admin.ModelAdmin):
    search_fields = ['title']


admin.site.register(Category, Search)
admin.site.register(Product, Search)
admin.site.register(Slider)
admin.site.register(Cart, Filter)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(CustomerUser)
