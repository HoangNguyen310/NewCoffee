from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('cart', CartController.as_view(), name='cart'),
    path('checkout/', CheckoutController.as_view(), name='checkout'),
    path('payment/', PaymentController.as_view(), name='payment'),
    path('addcart/', CartController.addcart, name='addcart'),
]
