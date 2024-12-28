def fibonacci_iterative(n):
    fib_sequence = [0, 1]  # Start with the first two Fibonacci numbers
    for _ in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Sum of the last two numbers
        fib_sequence.append(next_fib)
    return fib_sequence[:n]

# Example usage
n = int(input("Enter the number of Fibonacci numbers you want: "))
print("Fibonacci sequence:", fibonacci_iterative(n))
