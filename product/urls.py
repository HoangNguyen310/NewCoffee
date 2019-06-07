from django.urls import path
from .views import ProductController


app_name = 'product'

urlpatterns = [
    path('cate/<str:cate_slug>/', ProductController.product, name='product'),
    path('product/<str:product_slug>/', ProductController.detail, name='detail'),
    path('cate/', ProductController.all, name='cate'),
]
