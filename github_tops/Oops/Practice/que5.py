'''Create a class BankAccount with attributes account_number and balance. Add methods to deposit and withdraw money.'''

class BankAccount:

    def __init__(self, account_number, balance):
        self.a = account_number
        self.b = balance

    def deposit(self, amount):
        if amount > 0:
            self.b += amount
            print(f"Deposited ₹{amount} successfully.")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.b:
                self.b -= amount
                print(f"Withdrew ₹{amount} successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid amount for withdrawal.")

    def show_info(self):
        print(f"\nAccount Number: {self.a}")
        print(f"Account Balance: ₹{self.b}")

d = BankAccount(978787888, 10000)
d.show_info()
d.deposit(5000)
d.show_info()
d.withdraw(3000)
d.show_info()
