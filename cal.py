#  1. Create a calculator that performs +, -, ×, ÷ repeatedly until user enters “exit”.

def cul_num():
    n=int(input('enter the number'))
    m=int(input('enter a number'))
    o=input('enter the symbol')
    p=input('enter the number')
    while True:
        n=int(input('enter the number'))
        m=int(input('enter a number'))
        o=input('enter the symbol')
        if o=='+':
            print(n+m)
        elif o=='-':
            print(n-m)
        elif o=='*':
            print(n*m)
        elif o=='/':
            if n==0 and m==0:
                print('error')
            else:
                print(n/m) 
        elif o=='*':
            print(n*m)
        user=input('enter')
        if user=='exit':
            break    
cul_num()
# 2. Write a function that returns the nearest prime number for any input number.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(11))

n=10
high=n
low=n
while True:
        if is_prime(high):
            print(high)
            break
        if is_prime(low):
            print(low)
            break
        high+= 1
        low-=1




# 3.Function to repeatedly add digits until a single digit is obtained


def single_digit_sum(n):
    while n > 9:
        total = 0
        for digit in str(n):
            total += int(digit)
        n = total
    return n

num = int(input("Enter a number: "))
print("Single digit sum is:", single_digit_sum(num))