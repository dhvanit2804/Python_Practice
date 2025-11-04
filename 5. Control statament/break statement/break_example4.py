lives = 3

status = True

while status:
    num = int(input("Enter a number: "))
    lives -= 1
    if lives < 1:
        break