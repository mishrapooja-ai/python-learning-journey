class BankAccount:
    def __init__(self):
        self.__balance=1000
    def deposit(self,amount):
        self.__balance=self.__balance+amount   
        print("Money Deposited") 
account=BankAccount()        
account.deposit(500)