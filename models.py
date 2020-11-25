from django.db import models
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class shop(models.Model):
    name=models.CharField(max_length=100)                   #searchproduct

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to ='price_comparison', default="")

    def __str__(self):
        return self.product_name
