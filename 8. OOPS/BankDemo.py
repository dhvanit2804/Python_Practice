class Bank:

    def openAccount(self, acno, cname, balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print(f"Hello {cname} Your Account Number {acno} Is Opened With {balance} Rs.")
    
    def deposite(self, amount):
        self.balance=self.balance+amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Sorry You Need Another {amount-self.balance} More Rs. To Withdraw")

    def checkBalance(self):
        print(f"Current Balance : {self.balance}")

b1=Bank()
b1.openAccount(101, "Dhvanit", 1000)

while True:
    print("*"*50)
    print("1. Deposite")
    print("2. Withdraw")
    print("3. CheckBalance")
    print("4. Exit")