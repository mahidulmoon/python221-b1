
# value = "mahidul"
# try:
#     print("inside try 1")
#     print(int(value))
#     print("inside try 2")
# except ValueError:
#     print("This is a value error data conversion.")
# except Exception as e:
#     print("I can not able to do that.",str(e))
# finally:
#     print("This is the final section.")

# print("mahidul islam")

import os


file = ""

# userInput = input("Please Enter a number: ")

# def fileWork(fileData,inputData) :
#     # print(inputData)
#     file.write(inputData)
#     file.close()
#     try:
#         print("fileData1: ",file.read())
#     except Exception as e:
#         fileRead = open("./mahidul.txt","rt")
#         print("fileData2: ",fileRead.read())

#         confirmation = input("Do you want to delete the file?: ")
#         if confirmation == "yes":
#             os.remove("./mahidul.txt")
#             print("success")


# try:
#     file = open("./mahidul.txt","x")
#     print("SUccess")
#     fileWork(file,userInput)
# except FileExistsError:
#     print("Program can not able to create a file.")
#     print("inside exception")
#     file = open("./mahidul.txt","a")
#     fileWork(file,userInput)


print(os.path.exists("./mahidul.txt"))