"Write a Python program to count vowels in a given string."

vowels = "aeiouAEIOU"
count = 0
string = input("Enter a text: ")

for i in vowels:
    if i in string:
        count+=1

print(f"Vowels Of String: {count}")