# 1. Create a function to check whether a number is prime or not.

r=[20]
g=['prime' if all(x%y!=0 for y in range(2,x)) else 'not prime' for x in r]
print(g)
# 2. Create a function to print all prime numbers between a given range.

n=int(input("enter the number:"))
list=[x for x in range(1,n+1) if n%x==0]
if len(list)==2:
    print("prime")
else:
    print("not prime")

# 3. Create a function to implement swapcase functionality without using the built-in method.

def swap_case(text):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)  
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)  
        else:
            result += ch  
    return result


text = "HeLLo WoRLd 123!"
print("After swap case:", swap_case(text))

# 4. Create a function to find the factorial of a number

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))