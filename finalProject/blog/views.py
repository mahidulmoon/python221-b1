from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Todo
from django.contrib import messages

@login_required(login_url='/')
def blogPage(request):
    if request.method == "GET":
        return render(request,'index.html')
    elif request.method == "POST":
        title = request.POST["todotitle"]
        description = request.POST["tododescription"]

        try:
            Todo.objects.create(title=title,description=description)
            messages.success(request,"ToDo has been successfully created.")
        except Exception as e:
            messages.error(request,"Can not able to create todo "+str(e))
        
        return redirect('allblog')