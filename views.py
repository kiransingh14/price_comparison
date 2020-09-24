from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm

from .models import *

from .forms import  CreateUserForm



def registerPage(request):                                                  #create a registration form                                          
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request , 'price_comparison/register.html' , context)



def loginPage(request):
    context={}
    return render(request , 'price_comparison/login.html',context)
