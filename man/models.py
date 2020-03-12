from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField('Name', max_length=200)
    icon = models.CharField("Icon", max_length=150)
    color = models.CharField('Color', max_length=100)
    # author = models.ForeignKey(User, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name