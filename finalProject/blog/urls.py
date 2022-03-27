from django.urls import path
from .views import *
urlpatterns = [
    path("allblogs/",blogPage,name='allblog')
]
