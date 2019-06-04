from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('cart', CartController.as_view(), name='cart'),
    path('addcart/', CartController.add_cart, name='addcart'),
    path('empty-cart/', CartController.add_cart, name='empty-cart'),
    path('checkout/', CheckoutController.as_view(), name='checkout'),
    path('payment/', PaymentController.as_view(), name='payment'),

]
