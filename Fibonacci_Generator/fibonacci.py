def fibonacci(n):
    """Generate Fibonacci series up to n."""
    fib_series = []
    a, b = 0, 1
    while a < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = fibonacci(n)
    print(f"Fibonacci series up to {n}: {result}")
