'Generate Fibonacci sequence using loops.'

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        next_value = seq[i-1] + seq[i-2]
        seq.append(next_value)
    return seq[:n]

# Example usage:
n = 10
fib_sequence = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")