'Find the first non-repeating character - Return the first character that appears only once in a string.'

s = input("Enter a string: ")

for i in s:
    if s.count(i) == 1:
        print(i)
        break
    else:
        print("No non-repeating character found.")