'Create a class Calculator with methods add, subtract, multiply, and divide. Test all operations using objects.'

class Calculator:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Division by zero not allowed."

c = Calculator()

print("Addition:", c.add(10, 5))
print("Subtraction:", c.subtract(10, 5))
print("Multiplication:", c.multiply(10, 5))
print("Division:", c.divide(10, 5))