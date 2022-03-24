
from unicodedata import name
from django.urls import path
from .views import indexPage,anotherPage,dbDataShow,updateDelete,deleteObj

urlpatterns = [
    path('', indexPage,name="index"),
    path('another/', anotherPage,name="another"),
    path('dbData/', dbDataShow,name="dbData"),
    path('update/<int:pk>/', updateDelete,name="updatedelete"),
    path('delete/<int:sk>/', deleteObj,name="deleteData"),
]