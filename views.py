from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render , redirect
from .models import *


def registerPage(request):                                                  #create a registration form                                          
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request , 'price_comparison/register.html' , context)



def loginPage(request):
    context={}
    return render(request , 'price_comparison/login.html',context)
