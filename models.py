from django.db import models
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class find(models.Model):
    searchobject=models.CharField(max_length=100)
    save=models.BooleanField(default=False)
