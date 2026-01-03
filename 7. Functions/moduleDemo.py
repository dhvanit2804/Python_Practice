import udf

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit")
    print("*"*40)

    choice=int(input("Enter Your Choice: "))

    if choice==1:
        n1 = int(input("Enter Number: "))
        udf.oddeven(n1)
    elif choice==2:
        n1 = int(input("Enter Number: "))
        n2 = int(input("Enter Number: "))
        udf.maxoftwo(n1, n2)
    elif choice==3:
        n1 = int(input("Enter Number: "))
        n2 = int(input("Enter Number: "))
        n3 = int(input("Enter Number: "))
        udf.maxofthree(n1, n2, n3)
    elif choice==4:
        n1 = int(input("Enter Number: "))
        udf.prime(n1)
    elif choice==5:
        n1 = int(input("Enter Limit: "))
        udf.fibonacci(n1)
    elif choice==6:
        print("Exiting...")
        break
    else:
        print("Invalid Choice! Please Try Again.")
        