'Create a product dictionary and calculate total price.'

products = {
    'Laptop': 50000,
    'Mobile': 60000,
    'AC': 40000,
    'Car': 100000
}

total = 0

for price in products.values():
    total += price

print(total)