from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password','password2']