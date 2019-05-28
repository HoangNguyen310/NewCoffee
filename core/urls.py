from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeController.as_view(), name='index'),
    path('about/', AboutController.as_view(), name='about'),
    path('contact/', ContactController.as_view(), name='contact'),
]
