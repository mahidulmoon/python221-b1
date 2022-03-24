from assignment4 import fileDataSaveDynamic,getTime
dataFormat = dict()

def showOutput():
    print("\n\t==============00================")
    userInput = str(input("Do you want to save a file?(yes/no): "))
    if userInput == "yes":
        filename = "./"+str(dataFormat['univarsity'])+"("+str(dataFormat['department'])+").txt"
        datatosave = "\nTime : "+str(getTime())+"\nData: "+str(dataFormat)+"\n"
        fileDataSaveDynamic(datatosave,filename)
    elif userInput == "no":
        print("\n\tUnivarsity name: \t",dataFormat['univarsity'])
        print("\tDepartment \t",dataFormat['department'])
        for i in dataFormat['students']:
            print("\t  ID:\t"+str(i))
            print("\t  Name:\t"+str(dataFormat['students'][i]['name']))
            print("\t  Subject:\t"+str(dataFormat['students'][i]['subject']))
            print("\n")
    else:
        print("\n\nNOT A VALID INPUT")

def takeInput():
    print("\t==============00================")
    varsity = str(input("\tPlease Enter A University Name: "))
    dept = str(input("\tPlease Enter Department Name: "))
    studentName = ""
    iterationNumber = 1

    dataFormat["univarsity"] = varsity
    dataFormat["department"] = dept

    localDict = dict()
    while studentName != "end":
        print("\n\t\t=============="+str(iterationNumber)+"================")
        studentName = str(input("\t\tPlease Enter A Student Name: "))
        if studentName != "end":
            subjectName = str(input("\t\tPlease Select A Subject: "))
            studentInfo = {
                "name" : studentName,
                "subject" : subjectName
            }
            localDict.update({iterationNumber :studentInfo})
            iterationNumber+=1
        else:
            break
        
    dataFormat.update({"students":localDict})

if __name__ == "__main__":
    takeInput()
    showOutput()