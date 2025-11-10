# Dictionary sorting by keys
my_dict = {'b': 3, 'a': 1, 'c': 2}

sorted_dict = dict(sorted(my_dict.items()))
print("Sorted Dictionary by Keys:", sorted_dict)


# Find maximum value in a dictionary
my_dict = {'a': 10, 'b': 25, 'c': 7, 'd': 30}

max_value = max(my_dict.values())
print("Maximum Value:", max_value)


# Create alphabet to ASCII dictionary
ascii_dict = {chr(i): i for i in range(65, 91)}  # A to Z
print(ascii_dict)


# Dictionary of squares > 10
square_dict = {x: x**2 for x in range(1, 11) if x**2 > 10}
print(square_dict)
