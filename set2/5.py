list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

concatenated_list = [x + y for x, y in zip(list1, list2)] + list1[len(list2):] + list2[len(list1):]

print(concatenated_list)
