class Account:

    def __init__(self,title=None,balance=0):
        # write your code here
        self.title=title
        self.balance=balance
        

class SavingsAccount(Account):

    def __init__(self,title=None,balance=0,intrestrate=0):
        # write your code here
        super().__init__(title,balance)
        self.intrestrate=intrestrate

obj=Account("Ashish",5000)
obj=SavingsAccount("Ashish",5000,5)
