'Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal. '

def decimal_to_binary(n):
    return bin(n)

def decimal_to_octal(n):
    return oct(n)

def decimal_to_hexadecimal(n):
    return hex(n)

# Example usage:
decimal = 10
print(f"Decimal: {decimal}")
print(f"Binary: {decimal_to_binary(decimal)}")
print(f"Octal: {decimal_to_octal(decimal)}")
print(f"Hexadecimal: {decimal_to_hexadecimal(decimal)}")