'Find whether a number is Prime or not'
numbers = int(input("Enter a number: "))
is_prime = True

for i in range(2, numbers):
    if numbers % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{numbers} is a Prime number")
else:
    print(f"{numbers} is not a Prime number")