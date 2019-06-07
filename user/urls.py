from django.urls import path
from .views import *

app_name = 'user'

urlpatterns = [
    path('login/', LoginController.as_view(), name='login'),
    path('logout/', LogoutController.as_view(), name='logout'),
    path('register/', RegisterController.as_view(), name='register'),
    path('info/', InfoController.as_view(), name='info'),
    path('update_info/', InfoController.post, name='update_info')
]
