'Iterate through the first 10 numbers (0, 9). In each iteration, print the current number, the previous number, and their sum'

previous_num = 0
current_num = 0
sum = 0

for i in range(10):
    current_num = i
    previous_num = i - 1 if i > 0 else 0
    sum = current_num + previous_num
    print(f"Current Number: {current_num} Previous Number: {previous_num} Sum: {sum}")