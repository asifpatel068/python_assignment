def factorial(number):
    fact = 1
    
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return "Factorial of 0 is 1."
    else:
        for i in range(1, number + 1):
            fact *= i
    
    return fact

# Test the function
number = 5
result = factorial(number)
print("Factorial of", number, "is", result, ".")
