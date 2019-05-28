from django.urls import path
from .views import *
from django.contrib.auth import views

app_name = 'user'

urlpatterns = [
    path('login/', LoginController.as_view(), name='login'),
    path('logout/', LogoutController.as_view(), name='logout'),
    path('register/', RegisterController.as_view(), name='register'),
    path('info/', InfoController.as_view(), name='info'),
]
