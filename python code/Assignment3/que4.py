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

class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest {interest} added. New Balance: {self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_amount=500):
        super().__init__(account_holder, balance)
        self.overdraft_amount = overdraft_amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw Amount Must be Positive")
        elif amount > (self.balance + self.overdraft_amount):
            print("Overdraft Limit Executted")
        else:
            self.balance -= amount
            print(f"Withdrawing {amount}. Remaining Balance: {self.balance}")

saving = SavingAccount("Dhvanit", 10000, 0.10)
saving.check_balance()
saving.apply_interest()
saving.withdraw(200)

print("\n")

cheking = CheckingAccount("Dhvanit", 500, 1000)
cheking.check_balance()
cheking.withdraw(1200)
cheking.withdraw(500)