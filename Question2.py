# Challenge 2: Implement a Calculator Class

class calculator:
    def __init__(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))
    
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1

obj = calculator()
addition = obj.add()
subtraction = obj.subtract()
multiplication = obj.multiply()
division = obj.divide()
print(f"Addition: {addition}\nSubtraction: {subtraction}\nMultiplication: {multiplication}\nDivision: {division}")