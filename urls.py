from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.homePage,name="index"),
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('saveitems/',views.saveitemPage,name="save"),
    path('result/',views.resultPage,name="result"),
    path('about/',views.aboutPage,name="about")
]