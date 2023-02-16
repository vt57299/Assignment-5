# Challenge 3: Implement the complete student class

class Student:
    def __init__(self,__name,__rollnumber):
        self.__name = __name
        self.__rollnumber = __rollnumber
        print(f"Student Name: {self.__name}\nRoll number: {self.__rollnumber}")

    def setName(self,name):
        self.__name = name         
    def getName(self):
        return self.__name
   
    def setrollnumber(self,rollnumber):
        self.__rollnumber = rollnumber
    def getrollnumber(self):
        return self.__rollnumber
    
obj = Student("Viv",55)

# Printing Original values
print("Before change")
print(f"Name: {obj.getName()}")
print(f"Roll number: {obj.getrollnumber()}\n")

# Updating name and roll no.
obj.setName("Vivek")
obj.setrollnumber(60)

# Printing Updated values
print("After change")
print(f"Name: {obj.getName()}")
print(f"Roll number: {obj.getrollnumber()}")