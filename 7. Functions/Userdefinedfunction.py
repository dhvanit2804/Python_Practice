'Function With No Arguments & No Return Value'

def printLine():
    print("*"*50)

printLine()
print("Welcome to user-defined functions in Python")
printLine()

'Function With Arguments But No Return Value.'
def add(a, b):
    print(f"Addition : {a+b}")

printLine()
add(int(input("Enter a number: ")), int(input("Enter a number: ")))
printLine()

'Function With Arguments But & Return Value.'
def sub(a, b):
    return a - b

printLine()
print(f"Subtraction : {sub(int(input("Enter a number: ")), int(input("Enter a number: ")))}")
printLine()