class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposite Amount: {amount} New balance: {self.balance}")
        else:
            print("Deposite Amount Must be Positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw Amount Must be Positive")
        elif amount > self.balance:
            print("Insufficent Balance")
        else:
            self.balance -= amount
            print(f"Withdraw Amount: {amount} Remaining balance: {self.balance}")

    def check_balance(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Current Balance: {self.balance}")

acc1 = BankAccount("Dhvanit", 2000)
acc1.deposite(4000)
acc1.check_balance()
acc1.withdraw(1000)
acc1.check_balance()