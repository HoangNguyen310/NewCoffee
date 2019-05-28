from django.db import models
from user.models import CustomerUser
from cart.models import Cart


class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ship_address = models.CharField(max_length=255)
    order_description = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
