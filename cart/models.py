from django.db import models
from product.models import Product
from user.models import CustomerUser


class Cart(models.Model):
    user = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)

    def __str__(self):
        return self.user


class CartItem(models.Model):
    user = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.user

