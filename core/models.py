from django.db import models

class Slider(models.Model):
    title = models.CharField(default='New Coffee', max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='slide')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title