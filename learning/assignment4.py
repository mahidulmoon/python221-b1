from datetime import datetime

def getTime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def fileCreat():
    file=""
    try:
        file = open("./everyresult.txt","x")
        print("File created SuccessFully.")
    except Exception as e:
        print("File already Created")
    # file.close()

def fileCreateDynamic(name):
    file=""
    try:
        file = open("./"+str(name),"x")
        print("File created SuccessFully.")
    except Exception as e:
        print("File already Created")
    # file.close()


def fileDataSave(data_to_save):
    fileCreat()
    try:
        file = open("./everyresult.txt","a")
        file.write(data_to_save)
        file.close

    except Exception as e:
        print("can not able to write on file",str(e))

def fileDataSaveDynamic(data_to_save,filename):
    fileCreateDynamic(filename)
    try:
        file = open("./"+filename,"a")
        file.write(data_to_save)
        file.close

    except Exception as e:
        print("can not able to write on file",str(e))


def addition ():
    print("Addition")
    addition_list = []
    n = float(input("Enter the number: "))
    t = 0 
    ans = 0
    while n != 0:
        ans = ans + n
        addition_list.append(n)
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    fileDataSave("\nTime : "+str(getTime())+"\nAdditional result for "+str(addition_list)+" data is :"+str(ans)+"\n")
    return [ans,t]


def subtraction ():
    print("Subtraction")
    subtraction_list = []
    n = float(input("Enter the number: "))
    t = 0 
    ans = 0 
    while n != 0:
        ans = ans - n if t != 0 else n
        subtraction_list.append(n)
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    fileDataSave("\nTime : "+str(getTime())+"\nSubtraction result for "+str(subtraction_list)+" data is :"+str(ans)+"\n")
    return [ans,t]

def multiplication ():
    print("Multiplication")
    multiplication_list = []
    n = float(input("Enter the number: "))
    t = 0 
    ans = 1
    while n != 0:
        ans = ans * n
        multiplication_list.append(n)
        t+=1
        n = float(input("Enter another number (0 to calculate): "))
    fileDataSave("\nTime : "+str(getTime())+"\nMultiplication result for "+str(multiplication_list)+" data is :"+str(ans)+"\n")
    return [ans,t]

def average():
    an = []
    an = addition()
    t = an[1]
    a = an[0]
    ans = a / t
    fileDataSave("Average result for "+str(an)+" data is :"+str(ans)+"\n")
    return [ans,t]

def startProject():
    while True:
        list = []
        print(" My first python program!")
        print(" Simple Calculator in python by Md. Mahidul Islam")
        print(" Enter 'a' for addition")
        print(" Enter 's' for substraction")
        print(" Enter 'm' for multiplication")
        print(" Enter 'v' for average")
        print(" Enter 'q' for quit")
        c = input(" ")
        if c != 'q':
            if c == 'a':
                list = addition()
                print("Ans = ", list[0], " total inputs ",list[1])
            elif c == 's':
                list = subtraction()
                print("Ans = ", list[0], " total inputs ",list[1])
            elif c == 'm':
                list = multiplication()
                print("Ans = ", list[0], " total inputs ",list[1])
            elif c == 'v':
                list = average()
                print("Ans = ", list[0], " total inputs ",list[1])
            else:
                print ("Sorry, invilid character")
        else:
            break

if __name__ == "__main__":
    startProject()