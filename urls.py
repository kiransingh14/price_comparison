from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.homePage,name="index"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('saveitem/',views.saveitemPage,name="save"),
    path('result/',views.resultPage,name="result")
]