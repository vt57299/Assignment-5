# Challenge 5: Handling a Bank Account

class Account: 
    def __init__(self,title,AccountBalance):               # Initializing with title and account balance
        self.title = None                                  # Instance Variable
        self.AccountBalance = 0                            # Instance Variable

    def getbalance(self):
        return self.AccountBalance

    def deposit(self,amount):
        self.amount = amount
        self.AccountBalance = self.AccountBalance + self.amount                   # Updating the Account balance after deposit 
        return self.AccountBalance                            

    def withdrawal(self,amount):
        self.amount = amount 
        self.AccountBalance = self.AccountBalance - self.amount                  # Updating the Account Balance after withdrawal
        return self.AccountBalance

    def interestamount(self,interestRate): 
        self.interestrate = interestRate
        return (self.AccountBalance * self.interestrate)/100                     # returns Interest rate 

class SavingsAccount(Account):                           

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
print(f"Account Balance: { obj.getbalance()}")
print(f"Balance after Deposit: {obj.deposit(200)}")
print(f"Balance after Withdrawal: {obj.withdrawal(100)}")
print(f"Interest Amount: {obj.interestamount(7)}")