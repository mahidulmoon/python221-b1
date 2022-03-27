from cmath import log
from django.urls import path
from .views import loginPage,registerPage,logOut


urlpatterns = [
    path('',loginPage,name='loginpage'),
    path('register/',registerPage,name='registerpage'),
    path('logout/',logOut,name='logout'),
]
