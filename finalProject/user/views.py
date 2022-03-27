from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def loginPage(request):
    if request.method == "GET":
        return render(request,'html/login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"Login successful")
            return redirect('allblog')
        else:
            messages.error(request,"Invalid username and password")
            return redirect('loginpage')




def registerPage(request):
    if request.method == "GET":
        return render(request,'html/register.html')
    elif request.method == "POST":
        # print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        try:
            User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            messages.success(request,"User Creation successful")
            return redirect("loginpage")
        except Exception as e:
            messages.error(request,"can not create user"+str(e))
            return redirect("registerpage")