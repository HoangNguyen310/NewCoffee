from django.urls import path
from .views import ProductController


app_name = 'product'

urlpatterns = [
    path('product/<int:category_id>/', ProductController.product, name='product'),
    path('detail/<int:product_id>/', ProductController.detail, name='detail'),
]