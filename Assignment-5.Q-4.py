class Account:
   def __init__(self,title,balance):
      self.title=title
      self.balance=balance
   def name(self):
        # def description(self):
        return f"{self.title} , {self.balance} is the account balance "
      
class SavingAccount(Account):
   def __init__(self,interestRate):
      self.interestRate=interestRate
   def bank(self):
      return f"{self.interestRate} is the interestrate "
      
obj=Account(input("enter name of account holder :"),float(input("enter amount :")))


sa=SavingAccount(float(input("enter interestrate  :")))
print(obj.name())
print(sa.bank())