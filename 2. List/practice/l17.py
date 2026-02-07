'Separate even and odd numbers from a list.'

numbers = [17, 18, 19, 20, 22, 24, 25]

odd = []
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Odd numbers:", odd)
print("Even numbers:", even)
