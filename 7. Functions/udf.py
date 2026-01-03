def oddeven(a):
    if a % 2 == 0:
        print(f"{a} Even Number")
    else:
        print(f"{a} Odd Number")

def maxoftwo(a, b):
    if a>b:
        print(f"{a} is max")
    else:
        print(f"{b} is max")

def maxofthree(a, b, c):
    if a>b:
        if a>c:
            print(f"{a} is max")
        else:
            print(f"{c} is max")
    elif b>c:
        print(f"{b} is max")
    else:
        print(f"{c} is max")

def prime(a):
    if a%2 != 0:
        for i in range(3, int(a/2)+1, 2):
            if a%i == 0:
                print(f"{a} Is Not Prime")
                break
        else:
            print(f"{a} Is Prime")
    else:
        print(f"{a} Is Not Prime")

def fibonacci(n):
    a, b = 0,1
    print(a, end=" ")
    while b<n:
        print(b, end=" ")
        a,b=b, a+b
    print()
