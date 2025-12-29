'''Electricity Bill Calculator
Write a program to calculate the electricity bill based on the following:
For the first 100 units – ₹5 per unit
For the next 100 units – ₹8 per unit
For units above 200 – ₹10 per unit
Add ₹100 as a fixed charge to the total bill'''

units = int(input("Enter Electricity Units: "))

if units <= 100:
    amount = units * 5
elif units <= 200:
    amount = (100 * 5) + (units - 100) * 8
else:
    amount = (100 * 5) + (100 * 8) + (units - 200) * 10

total_bill = amount + 100
print(f"Total Electricity Bill: ₹{total_bill}")