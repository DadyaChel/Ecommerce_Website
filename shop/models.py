from django.db import models
from django.contrib.auth import get_user_model

from accounts.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=99)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name