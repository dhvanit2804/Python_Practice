'''Constructor Practice

Create a BankAccount class with account_number, balance, and owner_name. Implement deposit and withdrawal methods.'''

class BankAccount:

    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposite(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
        else:
            print(f"Sorry You Need Another {amount-self.balance} amount for withdraw this amount")

    def display(self):
        print("\n--- Owner's Information ---")
        print(f"Account Number : {self.account_number}")
        print(f"Name : {self.owner_name}")
        print(f"Balance : {self.balance}")

b = BankAccount(123456, 10000, "Dhvanit Parate")

b.deposite(5000)
b.withdraw(3000)
b.display()