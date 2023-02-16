# Challenge 1: Square Numbers and Return Their Sum

class point:
    def __init__(self):
        
        self.x = int(input("Enter first number: "))
        self.y = int(input("Enter second number: "))
        self.z = int(input("Enter third number: "))
     
    def sqSum(self):
       return (self.x**2+self.y**2+self.z**2)                               # squaring and adding those squares
       
       
obj = point()                                                               #   Creating object
print(f"Sum of squares of numbers you entered: {obj.sqSum()}")              # calling sqSum function and printing
