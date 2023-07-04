numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break  # Stop the loop if the number is greater than 500
    
    if num > 150:
        continue  # Skip the number if it is greater than 150
    
    if num % 5 == 0:
        print(num)
