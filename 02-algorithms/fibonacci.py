"""
Algorithm: Fibonacci Sequence
Generate Fibonacci numbers
"""

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence


if __name__ == "__main__":
    # Test
    num_terms = 10
    result = fibonacci(num_terms)
    print(f"First {num_terms} Fibonacci numbers: {result}")
