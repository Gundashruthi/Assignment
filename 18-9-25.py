#1.   for x in range(2,2):
            #   print(x) Output?


for x in range(2, 2):
    print(x)

# 2. Print numbers 5 4 3 2 1 using loop 

for i in range(5, 0, -1):
    print(i, end=' ')

# 3. Print prime number between 10 to 100 using while loop 

num = 10
while num <= 100:
    i = 2
    is_prime = True
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime and num > 1:
        print(num, end=' ')
    num += 1


# 4. Check given number perfect or not using while loop

num = int(input("Enter a number: "))
i = 1
sum_factors = 0

while i < num:
    if num % i == 0:
        sum_factors += i
    i += 1

if sum_factors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is Not a Perfect Number")
