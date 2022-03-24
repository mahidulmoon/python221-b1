# class Person:
#     def __init__(self,name,age):
#         self.humanName = name
#         self.humanAge = age

# human1 = Person("mahidul",27)
# print("Name: ",human1.humanName)

# print("Age: ",human1.humanAge)
# human1.humanAge = 36

# print("Age2: ",human1.humanAge)

# del human1.humanName

# print("name: ",human1.humanName)



class Car:
    def __init__(self,name,model,year):
        self.carName = name
        self.carModel = model
        self.year = year

        self.fuelCap = 15
    def checkFuel(self,newlevel):
        if self.fuelCap == newlevel:
            print("level are equal")
            self.fuelCap -= 1
        else:
            print("please refuel")

class Electric(Car):
    def __init__(self,name,model,year,battery):
        super().__init__(name,model,year)
        self.batteryUsage = battery


bmw = Car("BMW","m4",2017)
lambo = Car("Lamborgini","avendetor",2016)

print("BMW:",bmw.carName,bmw.fuelCap)
print("lambo:",lambo.carName,lambo.fuelCap)

# userInput = int(input("Fuel Level: "))
# bmw.checkFuel(userInput)
# print("new fuel bmw:",bmw.fuelCap)
# print("new fuel lambo:",lambo.fuelCap)


tesla = Electric("Tesla","a6","2015",70)
print("tesla:",tesla.batteryUsage)
print("tesla name:",tesla.carName)

userInput = int(input("Fuel Level: "))
tesla.checkFuel(userInput)
print("new fuel tesla:",tesla.fuelCap)