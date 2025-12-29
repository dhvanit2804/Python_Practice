'Create a class Laptop that has instance variables for brand, price, and a method discounted_price(discount_percent).'

class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discounted_price(self, discount_percent):
        discount = self.price * (discount_percent / 100)
        return self.price - discount
    
l = Laptop("Dell", 60000)
print(f"Original Price: ₹{l.price}")
print(f"Price after 10% discount: ₹{l.discounted_price(10)}")