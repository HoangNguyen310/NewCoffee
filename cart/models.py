from django.db import models
from product.models import Product
from user.models import CustomerUser


class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    total = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.user


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.cart


# class Item(models.Model):
#     product = models.CharField(max_length=100)
#     price = models.IntegerField()
#     quantity = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.product
