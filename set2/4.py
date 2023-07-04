str1 = "PyNaTive"

lowercase_letters = sorted([char for char in str1 if char.islower()])
uppercase_letters = sorted([char for char in str1 if char.isupper()])

sorted_str = ''.join(lowercase_letters + uppercase_letters)

print(sorted_str)
