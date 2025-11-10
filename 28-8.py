for i in range(1,11):
    print(i)

for i in range(2,21,2):
    print(i)


for i in range(1,21,2):
     print(i)


for i in range(10,0,-1):
    print(i)


for i in range(1,11):
    print(i,"square is",i*i)


a=5
for i in range(1,11):
    print(a,"x",i,"=",a*i)


total=0
for i in range(1,101):
    total += i
    print("sum=",total)


product=1
for i in range(1, 11): 
    product *= i 
print("Factorial of 10 =", product) 


for i in range(1, 51): 
    if i % 5 == 0: 
        print(i) 


for i in range(1,31):
    if i%2==0 and i%3==0:
        print(i)
n = int(input("\n enter n:"))

for i in range(1, 2*n, 2):
    print(i, end="")

n = int(input("\n enter n:"))
for i in range(2, 2*n+1, 2):
    print(i, end="")


n = int(input("\n enter n:"))
for i in range(n,0,-1):
    print(i, end="")


n = int(input("\n enter n:"))
for i in range(1,n+1, 2):
    print(i, end="")


n = int(input("\n enter n:"))
for i in range(1, n+1, 3):
    print(i, end="")


n=int(input("\n enter n:"))
for i in range(1,n):
    print(i,"square is",i*i)


n=int(input("\n enter n:"))
for i in range(1,n):
    print(i,"square is",i*i*i)

n=int(input("\n enter n:"))
product=n
for i in range(1, n): 
     product *= i 
print("Factorial of n =", product) 


n=int(input("enter n:"))
for i in range(1, n+1): 
     if i % 10 == 5: 
         print(i, end="")


n=int(input("\n enter n:"))
count=0
for i in range(1,n+1):
    if i % 4 == 0:
        count +=1
        print("count  divisble by 4:",count)


n=int(input("\n enter n:"))
count=0
for i in range(1,n+1):
    if i % 2 != 0:
        count +=1
        print("count not divisble by 2:",count)


n=int(input("\n enter n:"))
for i in range(2, n+1,2):
     print(i,"square is",i*i)


n=int(input("\n enter n:"))
for i in range(1,n+1,2):
     print(i,"square is",i*i*i)


n=int(input("enter n:"))
for i in range(1,n+1):
     if i%2==0 and i%3==0:
         print(i,end="")


         
n=int(input("enter n:"))
for i in range(1,n+1):
     if i%2==0 and i%5==0:
         print(i,end="")