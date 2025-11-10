# 1) Write a list comprehension in Python that checks whether each number in a given list is "prime" or "not prime" and returns the result as a list.

r=[20,33,45,54,3]
g=['prime' if all(x%y!=0 for y in range(2,x)) else 'not prime' for x in r]
print(g)
# 2)  Using list comprehension, generate a 2D list with the following structure
# input=[[1,2,3],[4,5,6],[7,8,9]] ==> output=[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

t=[[1,2,3],[4,5,6],[7,8,9]]
res=[[x[y]for x in t] for y in range(len(t[0]))]
print(res)

# 3)  Using list comprehension, generate a list of tuples mapping ASCII values to characters for uppercase letters A, B, C.

r=['A','B','C','a']
res=tuple((ord(x),x) for x in r if x.isupper())
print(res)