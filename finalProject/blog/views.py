from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Todo
from django.contrib import messages

@login_required(login_url='/')
def blogPage(request):
    if request.method == "GET":
        queryData = Todo.objects.all()
        contextData = {
            "data" : queryData,
        }
        return render(request,'index.html',contextData)
    elif request.method == "POST":
        title = request.POST["todotitle"]
        description = request.POST["tododescription"]

        imageFile = request.FILES['todofile']

        try:
            Todo.objects.create(title=title,description=description,created_by=request.user,img_file=imageFile)
            messages.success(request,"ToDo has been successfully created.")
        except Exception as e:
            messages.error(request,"Can not able to create todo "+str(e))
        
        return redirect('allblog')


@login_required(login_url='/')
def owntodo(request):
    if request.method == "GET":
        queryData = Todo.objects.filter(created_by=request.user)
        contextData = {
            "data" : queryData,
        }
        return render(request,'ownTodo.html',contextData)