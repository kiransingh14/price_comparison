from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .shopclues import *
from .amazon_in import *
from .models import *

from .forms import  *




data = []


# Create your views here.

def homePage(request):                                                #home page view
    shops = shop.objects.all()

    form = ShopForm()
    if request.method=='POST':
        form = ShopForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('result')
    context = {'shops':shops ,'form' :form}
    return render(request,'price_comparison/index.html',context)

def contact(request):
    if request.method=='POST':
        email = request.POST.get('name','')
        message = request.POST.get('name','')
        
        contact = Contact(email = email , message = message)
        contact.save()
    return render(request,'price_comparison/index.html')



def resultPage(request):                                             #result page
    if 'name' in request.POST:
        del extracted_data_amazon_india[:]
        del extracted_data_shopclues[:]
        hello = str(request.POST['query'])
        data = hello.split(",")
        i = 0
        while i < len(data):
            print("Inside link no" + str(i))
            Initial_shopclues(data[i])
            initialamazon_India(data[i])
            i = i + 1
        print("Hello finally out")

        print(extracted_data_shopclues)
        print (extracted_data_amazon_india)
    datamatch=zip(extracted_data_amazon_india,extracted_data_shopclues)
    context = {'datamatch':  datamatch}
    return render(request, 'price_comparison/result.html', context)
    
        


def registerPage(request):                                          # a registration form                                          
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('login')
    context = {'form' : form}
    return render(request , 'price_comparison/register.html' , context)



def loginPage(request):                                            # a login form

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username ,password=password) 
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Username OR Password is incorrect')
            
    context={}
    return render(request , 'price_comparison/login.html',context)

@login_required(login_url='login')                                 # a logout
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def saveitemPage(request):                                          #saved product
    context={}
    return render(request,'price_comparison/saveitems.html',context)

def aboutPage(request):                                            #about page
    context={}
    return render(request,'price_comparison/about.html',context)