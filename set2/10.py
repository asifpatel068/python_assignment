tuple1 = (11, [22, 33], 44, 55)

# Convert the nested list to a mutable list
nested_list = list(tuple1[1])

# Modify the first item in the list
nested_list[0] = 222

# Convert the list back to a tuple
modified_tuple = tuple1[:1] + (nested_list,) + tuple1[2:]

print("tuple1:", modified_tuple)
