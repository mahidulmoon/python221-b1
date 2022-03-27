from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def blogPage(request):
    return render(request,'blogIndex.html')