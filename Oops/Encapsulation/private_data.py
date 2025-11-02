class BankAccount:
    
    def __init__(self, account_holder, balance):
        #Public Attribute
        self.account_holder = account_holder
        #Private Attribute
        self.__balance = balance

    # Public method to access private attribute (getter method)
    def get_balance(self):
        return self.__balance

    # Public method to modify private attribute (setter method)
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount} successfully.")
        else:
            print("Deposite amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ₹{amount} successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid amount for withdrawal.")

account = BankAccount("Dhvanit", 10000)

print(account.account_holder)

print(account.get_balance())

account.deposite(5000)
print(account.get_balance())

account.withdraw(3000)
print(account.get_balance())

print(account._BankAccount__balance)