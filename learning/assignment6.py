from datetime import datetime



class RecordObject:
    def __init__(self,name,dept):
        self.varsity = name
        self.deptName = dept

    def getTime(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

    def fileCreateDynamic(self,name):
        file=""
        try:
            file = open("./"+str(name),"x")
            print("File created SuccessFully.")
        except Exception as e:
            print("File already Created")
        # file.close()
    def fileDataSaveDynamic(self,data_to_save,filename):
        self.fileCreateDynamic(filename)
        try:
            file = open("./"+filename,"a")
            file.write(data_to_save)
            file.close

        except Exception as e:
            print("can not able to write on file",str(e))

    def updateStudent(self,studentsData):
        self.students = studentsData
    
    def formatedData(self):
        return {"university" : self.varsity,"department" :self.deptName,"students" : self.students}
    # def __str__(self) :
    #     return self

    def showOutput(self):
        print("\n\t==============00================")
        userInput = str(input("Do you want to save a file?(yes/no): "))
        if userInput == "yes":
            filename = "./"+str(self.varsity)+"("+str(self.deptName)+").txt"
            datatosave = "\nTime : "+str(self.getTime())+"\nData: "+str(self.formatedData())+"\n"
            self.fileDataSaveDynamic(datatosave,filename)
        elif userInput == "no":
            print("\n\tUnivarsity name: \t",self.varsity)
            print("\tDepartment \t",self.deptName)
            for i in self.students:
                print("\t  ID:\t"+str(i))
                print("\t  Name:\t"+str(self.students[i]['name']))
                print("\t  Subject:\t"+str(self.students[i]['subject']))
                print("\n")
        else:
            print("\n\nNOT A VALID INPUT")


def takeInput():
    print("\t==============00================")
    varsity = str(input("\tPlease Enter A University Name: "))
    dept = str(input("\tPlease Enter Department Name: "))
    studentName = ""
    iterationNumber = 1

    recordData = RecordObject(varsity,dept)

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
        
    recordData.updateStudent(localDict)
    recordData.showOutput()



if __name__ == "__main__":
    takeInput()