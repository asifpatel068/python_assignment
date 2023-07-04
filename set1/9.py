def fibonacci(n):
    sequence = []
    
    if n <= 0:
        return "Invalid input. Please provide a positive integer."
    elif n == 1:
        sequence.append(0)
    elif n == 2:
        sequence.extend([0, 1])
    else:
        sequence.extend([0, 1])
        for i in range(2, n):
            next_number = sequence[i-1] + sequence[i-2]
            sequence.append(next_number)
    
    return sequence

# Test the function
n = 5
fib_sequence = fibonacci(n)
print(fib_sequence)
