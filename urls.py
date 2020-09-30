from django.urls import path

from . import views

urlpatterns = [
    path('home/',views.homePage,name="home"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('saveitem/',views.saveitemPage,name="save")
]