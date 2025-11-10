numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total += num

print("Sum of elements:", total)


my_list = [1, 2, 2, 3, 4, 4, 4, 5]
freq = {}

for item in my_list:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Frequency of elements:", freq)


my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("List after removing duplicates:", unique_list)


list1 = [1, 2, 3]
list2 = [4, 5, 6]

merged = [*list1, *list2]  # unpacking operator

print("Merged List:", merged)
