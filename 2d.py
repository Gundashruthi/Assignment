# 1.	Flatten a 2D list into a 1D list using list comprehension.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)

# 2.	Extract all digits from a given string.

s = "abc123def456"
digits = [ch for ch in s if ch.isdigit()]
print(digits)

                                           
# 3.	Create a list of all numbers from 1–100 that are divisible by both 3 and 5.

nums = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
print(nums)

# 4.	Build a list of tuples (number, square) for numbers from 1–10.

squares = [(n, n**2) for n in range(1, 11)]
print(squares)

# 5.	Print prime numbers between 10 to 50 using list comprehension ?

primes = [n for n in range(10, 51) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print(primes)
