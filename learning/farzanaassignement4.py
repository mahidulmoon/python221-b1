def intro():
    print("My first python program!\nSimple calculator in python by Farjana Akter\nEnter 'a' for addition\nEnter 's' for subtraction\nEnter 'm' for multiplication\nEnter 'v' for average\nEnter 'q' for quit")
    global info
    info=input()
def ending():
    print("File already created")
    print("Ans=",result, "Total inputs:",count)
    print("=================")
    intro()
intro()

while info!="q":
    if info=='a':
        print("Addtion")
        value=float(input("Enter the number:"))
        result=value
        count=0
        while value!=0:
            value=float(input("Enter another number (0 to calculate):"))
            result+=value
            count+=1
        else:
            ending()
    elif info=='s':
        print("Subtraction")
        value=float(input("Enter the number:"))
        result=value
        count=0
        while value!=0:
            value=float(input("Enter another number (0 to calculate):"))
            result-=value
            count+=1
        else:
            ending()
    elif info=='m':
        print("Multiplication")
        value=float(input("Enter the number:"))
        result=value
        count=0
        while value!=0:
            value=float(input("Enter another number (0 to calculate):"))
            result*=value
            count+=1
        else:
            ending()
    elif info=='v':
        print("Average")
        value=float(input("Enter the number:"))
        result=value
        count=0
        while value!=0:
            value=float(input("Enter another number (0 to calculate):"))
            result+=value
            count+=1
            result1=result/count
        else:
            print("File already created")
            print("Ans=",result1, "Total inputs:",count)
            intro()
else:
    print("Can not go further")