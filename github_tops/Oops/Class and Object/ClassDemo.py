class MyClass:

    x=0
    def __init__(self,x):
        self.x=x

    def my_method(self):
        print(f"X: {self.x}")

    def OddEven(self):
        if self.x % 2==0:
            print(f"{self.x} Is even number")
        else:
            print(f"{self.x} Is odd number")

x = int(input("Enter the value of X: "))

a = MyClass(x)
a.my_method()
a.OddEven()