'''Create a BankAccount class with:

Private attributes: __balance, __account_number
Methods: deposit(), withdraw(), get_balance()
Implement proper validation (no negative deposits/withdrawals)'''

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number
        self.__balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposite Successfully")
        else:
            print("Invalid Amount Please Try Again With Valid Amount")

    def withdraw(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
            print("Amount Withdraw Successfully")
        else:
            print("Invalid Amount Please Try Again With Valid Amount")

    def get_balance(self):
        return self.__balance
    
b = BankAccount(123456)

b.deposite(10000)
b.withdraw(2000)
print(b.get_balance())