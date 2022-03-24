from cmath import log
from django.urls import path
from .views import loginPage


urlpatterns = [
    path('',loginPage,name='loginpage'),
]
