'''From a dictionary of employees and salaries, find:

Highest salary
Lowest salary
Average salary'''

employees = {"Alice": 50000, "Bob": 60000, "Charlie": 55000}
highest_salary = max(employees.values())
lowest_salary = min(employees.values())
average_salary = sum(employees.values()) / len(employees)

print(f"Highest Salary: {highest_salary}")
print(f"Lowest Salary: {lowest_salary}")
print(f"Average Salary: {average_salary}")