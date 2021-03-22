from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['uploaded']