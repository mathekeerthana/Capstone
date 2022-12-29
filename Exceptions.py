'''# Exceptions
#def Exception(self,a,b):
try:
    num1=int(input("Enter first number"))
    num2=int(input("Enter second number"))
    result=num1/num2
    print(result)
except ValueError:
    print("only integers")
except ZeroDivisionError:  # handle the Exceptions
    print("Divide by zero")'''


# Bank
class NegativeAmount(Exception):
    pass
class HigherAmount(Exception):
    pass

class Bank_Account:

    def Balance_check(self,balance):
        self.balance=balance
        print("Balance is:",balance)

    def Deposit_money(self,deposit):
        try:
             self.deposit = int(input("Enter Deposit amount"))
                if(deposit<=1000):
                    print("the deposit amount is",deposit)
                else:
                    print("amount greaterthan the deposit amount")


        def withdraw_amount(self,withdraw):
            self.withdraw =int(input("Enter withdraw amount"))
            if(withdraw < 100):
                print("withdraw amonut is",withdraw)

bankobj=Bank_Account
bankobj.Balance_check()
bankobj.Deposit_money()
bankobj.withdraw_amount()





