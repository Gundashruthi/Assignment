num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
sum_val = 0

while temp > 0:
    digit = temp % 10
    sum_val += digit ** digits
    temp //= 10

if num == sum_val:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


n = int(input("Enter a number: "))
print("Factors of", n, "are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial of", n, "is:", fact)


n = int(input("Enter a number: "))
count = 0
temp = n

while temp > 0:
    temp //= 10
    count += 1

print("Number of digits in", n, "is:", count)


