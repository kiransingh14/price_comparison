from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


from .models import *

from .forms import  CreateUserForm




data = []


# Create your views here.

def homePage(request):
    context = {}
    return render(request,'price_comparison/index.html',context)


def resultPage(request):
    context = {}
    return render(request,'price_comparison/result.html',context)





def registerPage(request):                                                  #create a registration form                                          
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
    context = {'form' : form}
    return render(request , 'price_comparison/register.html' , context)



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username ,password=password) 
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username OR Password is incorrect')
            
    context={}
    return render(request , 'price_comparison/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def saveitemPage(request):
    context={}
    return render(request,'price_comparison/saveitems.html',context)