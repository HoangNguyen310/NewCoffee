from django.db import models
from cart.models import Cart


class Order(models.Model):
    user = models.CharField(max_length=100)
    product = models.TextField(blank=True)
    ship_address = models.TextField()
    description = models.TextField(blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user
