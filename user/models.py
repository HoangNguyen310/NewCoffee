from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    phone = models.CharField(default='', max_length=15, blank=True)
    address = models.TextField(default='', max_length=255, blank=True)
