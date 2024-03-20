def fibonacci_sequence(n):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with first two terms

    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next term
        fib_sequence.append(next_term)

    return fib_sequence[:n]

# Example usage:
n = 10  # Specified term
fibonacci_series = fibonacci_sequence(n)
print("Fibonacci sequence up to term", n, ":", fibonacci_series)
