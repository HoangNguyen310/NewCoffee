from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('cart', CartController.as_view(), name='cart'),
    path('add-cart/', CartController.add_cart, name='addcart'),
    path('update-cart/', CartController.update_cart, name='update_cart'),
    path('remove-cart/', CartController.remove_cart, name='remove_cart'),
    path('empty-cart/', CartController.add_cart, name='empty_cart'),
    path('checkout/', CheckoutController.as_view(), name='checkout'),
    path('payment/', PaymentController.as_view(), name='payment'),
    path('pay/', PaymentController.post, name='pay'),

]
