from django.db import models
from django.conf import settings
import django.utils.safestring as safestring


class Category(models.Model):
    title = models.CharField(default='', max_length=100)
    slug = models.CharField(default='', max_length=100, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(default='', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product')
    price = models.IntegerField(default=0)
    sale = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def image_tag(self):
        if self.image:
            return safestring.mark_safe('<img src="%s%s" width="150" height="150"/>' % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title
