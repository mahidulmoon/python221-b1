from django.shortcuts import render,redirect,get_object_or_404
from .models import Office
# Create your views here.


def indexPage(request):
    sample_context = {
        'experience' : [
            {
                "comapny" : "Datasoft",
                "tech" : "React Django",
                "designation" : "software developer"
            },
            {
                "comapny" : "Doodle Inc",
                "tech" : "React Django Nodejs AWS",
                "designation" : "software developer"
            },
            {
                "comapny" : "Upskill",
                "tech" : "Vuejs Golang AWS",
                "designation" : "software developer"
            },
            {
                "comapny" : "abc",
                "tech" : "Vuejs Golang AWS",
                "designation" : "software developer"
            }
        ]
    }
    # context = {
    #     "name" : "Md. Mahidul Islam Moon"
    # }
    return render(request,'webapp/index.html',sample_context)



def anotherPage(request):
    return render(request,'webapp/another.html')


def dbDataShow(request):

    if request.method == "GET":
        queryset = Office.objects.all()
        context = {
            "data" : queryset
        }
        return render(request,'webapp/dbDataShow.html',context)
    elif request.method == "POST":
        company_name = request.POST["company_input"]
        designation_input = request.POST["designation_input"]
        image = request.FILES['photo']
        Office.objects.create(company_name=company_name,designation=designation_input,img_up=image)

        # tableData = Office(company_name=company_name,designation=designation_input)
        # tableData.save()


        return redirect('dbData')

def updateDelete(request,pk):
    # print("inside updatedelete view",pk)
    if request.method == "GET":
        # exactData = get_object_or_404(Office,id=pk)
        exactData = Office.objects.get(id=pk)

        contextDict = {
            "data" : exactData
        }

        return render(request,'webapp/updateTemplate.html',contextDict)
    else:
        # print("inside updatedelete view",pk)
        exactData = Office.objects.get(id=pk)
        company = request.POST['company_input']
        designation = request.POST['designation_input']

        exactData.company_name = company
        exactData.designation = designation

        exactData.save()

        return redirect('dbData')

def deleteObj(request,sk):
    exactData = Office.objects.get(id=sk)
    exactData.delete()
    return redirect('dbData')

