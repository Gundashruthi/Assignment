dict_list = []
n = int(input("Enter how many dictionaries you want to add: "))


for i in range(n):
    print(f"\nEnter details for dictionary {i+1}:")
    d = {} 
    keys = int(input("How many key-value pairs you want to add? "))

    for j in range(keys):
        key = input(f"Enter key {j+1}: ")
        value = input(f"Enter value for '{key}': ")
        d[key] = value  

    dict_list.append(d) 
print("\nList of Dictionaries:")
print(dict_list)
