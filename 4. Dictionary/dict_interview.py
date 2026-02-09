'''Problem:
You are given a list of transactions.
Each transaction has a user name and an amount spent.

transactions = [
    ("Alice", 200),
    ("Bob", 150),
    ("Alice", 300),
    ("Bob", 100),
    ("Charlie", 400),
    ("Alice", 100)
]
🎯 Tasks:
1. Create a dictionary that stores the total amount spent by each user

2. Find:
The user who spent the most
The user who spent the least

3. Print the results in this format:

Alice -> 600
Bob -> 250
Charlie -> 400
Highest spender: Alice
Lowest spender: Bob'''

transactions = [
    ("Alice", 200),
    ("Bob", 150),
    ("Alice", 300),
    ("Bob", 100),
    ("Charlie", 400),
    ("Alice", 100)
]

'1. Create a dictionary that stores the total amount spent by each user'

total_amount = {}

for key, value in transactions:
    if key in total_amount:
        total_amount[key] += value
    else:
        total_amount[key] = value

print(total_amount)

'''
2.Find:
The user who spent the most
The user who spent the least
'''

most_spent = max(total_amount, key=total_amount.get)
print(f"The Most Spent User is {most_spent} : {total_amount[most_spent]}")

least_spent = min(total_amount, key=total_amount.get)
print(f"The Least Spent User is {least_spent} : {total_amount[least_spent]}")

'3. Print the results in this format:'

for i in total_amount:
    print(f"{i} -> {total_amount[i]}")

print(f"Highest spender: {most_spent}")
print(f"Lowest spender: {least_spent}")