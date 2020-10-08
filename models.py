from django.db import models
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class shop(models.Model):
    name=models.CharField(max_length=100)
    search=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name