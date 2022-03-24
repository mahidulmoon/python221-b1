class Dog():
    def __init__(self,name,color):
        self.dogname = name
        self.color = color
    def printName(self):
        print("Hi",self.dogname)

    def showColor(self):
        print("Color: ",self.color)


my_dog = Dog("Tommy","black")
my_dog.printName()
my_dog.showColor()

my_dog2 = Dog("Jonny","white")
my_dog2.printName()
my_dog2.showColor()