from django.urls import path
from .views import mainContent,anotherContent
urlpatterns = [
    path('main/',mainContent,name='maincontent'),
    path('another/',anotherContent,name='anothercontent'),
]
