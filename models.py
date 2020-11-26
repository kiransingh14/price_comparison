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

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    email =  models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500 ,default="")

    def __str__(self):
        return self.email