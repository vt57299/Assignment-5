# Challenge 4: Implement a Banking Account

class Account:                                            

    def __init__(self,title,AccountBalance):               # Initializing with title and account balance
        self.title = None                                  # Instance Variable
        self.AccountBalance = 0                            # Instance Variable

class SavingsAccount(Account):                             # Inheriting "Account" class

    def __init__(self, title, AccountBalance,interestRate):      
        self.interestRate = interestRate
        super().__init__(title, AccountBalance)

# Overriding title and account balance
        self.title = title                                 
        self.AccountBalance = AccountBalance

    def display(self):                                     
       return f"Name: {self.title}\nAccount Balance: {self.AccountBalance}\nInterest rate: {self.interestRate}"
    
    
obj = SavingsAccount("Demo",5000,7)
print(obj.display())
